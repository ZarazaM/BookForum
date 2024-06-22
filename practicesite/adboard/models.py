from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Ad(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('ad-detail', kwargs={'pk': self.pk})
