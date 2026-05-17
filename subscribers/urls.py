from django.urls import path
from .views import subscribe, ask_question

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('ask/', ask_question, name='ask_question'),
]