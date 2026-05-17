from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
    
    def __str__(self):
        return self.email

class QuestionToEditor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    question = models.TextField(verbose_name='Вопрос')
    asked_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Вопрос редакции'
        verbose_name_plural = 'Вопросы редакции'
    
    def __str__(self):
        return f'Вопрос от {self.name}'