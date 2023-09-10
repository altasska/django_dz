from django.urls import path
from main.views import home, contacts

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('contacts/', contacts, name='contacts'),  # Страница контактов
]