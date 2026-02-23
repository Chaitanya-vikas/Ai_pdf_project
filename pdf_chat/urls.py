from django.urls import path
from .views import chat_with_pdf

urlpatterns = [
    path('chat-pdf/', chat_with_pdf, name='chat_with_pdf'),
]