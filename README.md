# Multi PDF RAG Chatbot

## Overview

A Streamlit-based chatbot that allows users to upload multiple PDF documents and ask questions based on their content. The application extracts text from the uploaded PDFs and uses Google's Gemini API to generate answers using the provided document context.

## Features

* Upload multiple PDF files
* Extract text from uploaded PDFs
* Ask questions based on PDF content
* AI-powered responses using Gemini
* User-friendly Streamlit interface

## Technologies Used

* Python
* Streamlit
* PyPDF2
* Google Gemini API
* python-dotenv

## Project Workflow

1. User uploads one or more PDF files.
2. Text is extracted from all uploaded PDFs.
3. User enters a question.
4. Extracted PDF content and the question are sent to Gemini.
5. Gemini generates an answer based on the uploaded PDF content.

## Installation and Setup

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a .env File

Create a file named `.env` in the project root directory and add:

```env
MY_API_KEY=your_gemini_api_key
```

### 5. Run the Application

```bash
streamlit run app.py
```

### 6. Open the Application

Streamlit will automatically provide a local URL, usually:

```text
http://localhost:8501
```

Open it in your browser to use the chatbot.


## Future Enhancements

* Chunking
* Embeddings
* Vector Database Integration
* Semantic Search
* Complete RAG Pipeline