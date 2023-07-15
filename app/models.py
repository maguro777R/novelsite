from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sakusya = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=70000)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateField(auto_now=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ('-published_date',) # 記事の並び順。新しいものから順に並ぶ

    def __str__(self):
        return self.title

'''
class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=70000)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ('-published_date',) # 記事の並び順。新しいものから順に並ぶ

    def __str__(self):
        return self.title
'''