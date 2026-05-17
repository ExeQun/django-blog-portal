from django.shortcuts import redirect
from django.contrib import messages
from .models import Subscriber, QuestionToEditor

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            obj, created = Subscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, 'Вы успешно подписались на рассылку!')
            else:
                messages.info(request, 'Вы уже подписаны на рассылку')
        else:
            messages.error(request, 'Введите email')
    return redirect('/')

def ask_question(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')
        
        if name and email and question:
            QuestionToEditor.objects.create(
                name=name,
                email=email,
                question=question
            )
            messages.success(request, 'Ваш вопрос отправлен редакции!')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля')
    return redirect('/')