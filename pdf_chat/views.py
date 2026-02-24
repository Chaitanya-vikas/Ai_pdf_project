from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import extract_text_from_pdf, get_ai_response
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def chat_with_pdf(request):
    pdf_file = request.FILES.get('document')
    user_query = request.data.get('question')

    if not pdf_file or not user_query:
        return Response({"error": "Please provide both a PDF 'document' and a 'question'."}, status=400)

    extracted_text = extract_text_from_pdf(pdf_file)
    
    if not extracted_text:
        return Response({"error": "No text found. This PDF might be a scanned image. Please upload a text-based PDF."}, status=400)

    try:
        ai_answer = get_ai_response(extracted_text, user_query)
        return Response({
            "status": "success",
            "question": user_query,
            "answer": ai_answer
        })
    except Exception as e:
        return Response({"error": f"AI processing failed: {str(e)}"}, status=500)