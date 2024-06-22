from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse

class Chat(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    create_time = models.DateTimeField(default=timezone.now, blank=True, verbose_name='Время создания')
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название'


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
    pub_time = models.DateTimeField(default=timezone.now, blank=True, verbose_name='Время отправки')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.text
