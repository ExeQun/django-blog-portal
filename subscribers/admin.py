from django.contrib import admin
from .models import Subscriber, QuestionToEditor

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']

@admin.register(QuestionToEditor)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'asked_at', 'is_answered']