import streamlit as st
from PyPDF2 import PdfReader
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("MY_API_KEY")
client = genai.Client(api_key=API_KEY)


def ask_gemini(question, pdf_text):
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using only the PDF content provided below.

PDF Content:
{pdf_text}

User Question:
{question}

If the answer is not available in the provided PDF content, respond with:

"There is no information in the uploaded PDF content related to your question."
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


st.title("Multi PDF RAG Chatbot")

files = st.file_uploader(
    "Upload PDF(s)",
    type="pdf",
    accept_multiple_files=True
)

if files:
    st.success("PDF(s) uploaded successfully.")
    pdf_text = ""

    for file in files:
        reader = PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                pdf_text += page_text + "\n"

else:
    st.error("Please upload at least one PDF.")

question = st.text_input("Ask a question:")

if st.button("Ask"):

    if not files:
        st.error("Please upload at least one PDF.")

    elif question.strip() == "":
        st.error("Please enter a question.")

    else:
        with st.spinner("Generating answer..."):
            answer = ask_gemini(question, pdf_text)

        st.subheader("Answer")
        st.write(answer)