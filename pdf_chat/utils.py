import PyPDF2
from google import genai
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        # 1. Rewind the file pointer to the very beginning
        pdf_file.seek(0) 
        
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
                
        # 2. Check if the PDF was just images/scans
        if not text.strip():
            print("DEBUG: PyPDF2 ran successfully, but found ZERO text. The PDF might be a scanned image.")
            return None
            
        return text
    except Exception as e:
        # 3. Print the exact error to your terminal so we can see it
        print(f"DEBUG PDF ERROR: {str(e)}")
        return None

def get_ai_response(document_text, user_query):
    # Fetch the secure key from the environment
    api_key = os.getenv("GEMINI_API_KEY")
    
    # Initialize the client with the secure key
    client = genai.Client(api_key=api_key) 
    
    prompt = f"""
    Use the following document text to answer the user's question.
    
    Document Text:
    {document_text}
    
    User Question: {user_query}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text