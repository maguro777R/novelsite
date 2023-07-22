from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField('タグ', max_length=59)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sakusya = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, verbose_name='タイトル')
    text = models.TextField(max_length=70000, verbose_name='本文')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='作成日')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='公開日')
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name='更新日')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='公開状態')
    category = models.ForeignKey(
        Category, verbose_name='カテゴリー',
        on_delete=models.PROTECT
    )
    tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True, null=True)
    relation = models.ManyToManyField('self', verbose_name='関連', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ('-published_date',) # 記事の並び順。新しいものから順に並ぶ

    def __str__(self):
        return self.title