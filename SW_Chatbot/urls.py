"""
URL configuration for SW_Chatbot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import chatbotAdmin.views

urlpatterns = [
    path('admin_page/', chatbotAdmin.views.admin_page, name='admin_page'),
    path('management/', chatbotAdmin.views.management, name='management'),
    path('add_notice/', chatbotAdmin.views.add_notice, name='add_notice'),
    path('add_question_answer/', chatbotAdmin.views.add_question_answer, name='add_question_answer'),
    path('chatbot_db_management/', chatbotAdmin.views.chatbot_db_management, name='chatbot_db_management'),
    path('admin/', admin.site.urls),
]
