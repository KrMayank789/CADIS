import streamlit as st
import os
import tempfile
from dotenv import load_dotenv


from rag_app import process_document, create_rag_chain

load_dotenv()

st.set_page_config(page_title="Document Intelligence", page_icon="📄")
st.title("📄 C-A-D-I-S")


if "messages" not in st.session_state:
    st.session_state.messages = []
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None


with st.sidebar:
    st.header("1. Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file and st.button("Process Document"):
        with st.spinner("Building Vector Database..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tf:
                tf.write(uploaded_file.getbuffer())
                temp_path = tf.name
            

            retriever = process_document(temp_path)
            st.session_state.rag_chain = create_rag_chain(retriever)
            
            st.success("Document processed! You can now chat.")
            os.remove(temp_path) 


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about the document..."):
    if st.session_state.rag_chain is None:
        st.error("Please upload and process a document in the sidebar first!")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("Searching document..."):
                response = st.session_state.rag_chain.invoke(prompt)
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})