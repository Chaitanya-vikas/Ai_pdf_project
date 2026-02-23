from django.contrib import admin
from django.urls import path, include
from pdf_chat.views import index # Import your new view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pdf_chat.urls')), # API routes
    path('', index, name='home'), #new Frontend route
]