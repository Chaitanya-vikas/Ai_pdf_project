import PyPDF2
from google import genai

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        return None

def get_ai_response(document_text, user_query):
    # Insert your actual API key here
    client = genai.Client(api_key="") 
    
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