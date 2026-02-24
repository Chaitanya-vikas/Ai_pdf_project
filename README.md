# AI-Powered PDF Intelligence 🚀

![Live on Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Gemini API](https://img.shields.io/badge/AI-Google_Gemini-4285F4?style=for-the-badge)

**Live Demo:** [View the Live Application Here](https://ai-pdf-project.onrender.com/)

## 📌 Project Overview
A full-stack, AI-driven web application that allows users to securely upload PDF documents and extract insights using natural language. Built with a robust Django backend and a modern Glassmorphism frontend, this application utilizes the Google Gemini API to process document text and generate accurate, context-aware responses to user queries.

This project demonstrates production-ready backend development, third-party API integration, secure environment management, and RESTful architecture.

## ✨ Key Features
* **AI-Driven Document Analysis:** Integrates Google's Gemini 2.5 Flash model for lightning-fast reading comprehension and Q&A.
* **RESTful API Backend:** Clean, decoupled architecture using Django and Django REST Framework to handle file uploads and JSON responses.
* **Robust PDF Extraction:** Utilizes `PyPDF2` to parse document text, complete with error handling for scanned or unreadable files.
* **Modern UI/UX:** A responsive, dark-mode frontend featuring pure CSS Glassmorphism and asynchronous JavaScript fetch requests.
* **Secure Architecture:** Production-ready configuration using `python-dotenv` to protect API keys and Gunicorn for deployment.

## 🛠️ Tech Stack
* **Backend:** Python, Django, Django REST Framework
* **AI Engine:** Google GenAI SDK (Gemini API)
* **Document Processing:** PyPDF2
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (ES6+)
* **Deployment & DevOps:** Render, Gunicorn, Git, GitHub

---

## 💻 Local Installation & Setup

If you would like to run this project locally, follow these steps:

**1. Clone the repository**
```bash
git clone (https://github.com/Chaitanya-vikas/Ai_pdf_project)
cd ai-pdf-intelligence

**2. Set up a virtual environment**
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

**3. Install dependencies**
pip install -r requirements.txt

**4. Set up Environment Variables
Create a .env file in the root directory and add your Google Gemini API key:
GEMINI_API_KEY=your_actual_api_key_here

**5. Run database migrations**
python manage.py migrate

The application will now be running at http://127.0.0.1:8000/
```

**🔌 API Documentation**
POST /api/chat-pdf/
Accepts a PDF document and a text query, returning an AI-generated answer.

Request payload (multipart/form-data):

document: The PDF file to be analyzed.

question: The user's text query (e.g., "Summarize this report").

Success Response (200 OK):

JSON
{
    "status": "success",
    "question": "Summarize this report",
    "answer": "The report indicates a 20% increase in Q3 revenue..."
}
Error Response (400 Bad Request):

JSON
{
    "error": "No text found. This PDF might be a scanned image."
}

## 📸 Screenshots
![Ai_Pdf](https://github.com/user-attachments/assets/b2cece73-c555-413d-b540-54ffd4cf1799)

