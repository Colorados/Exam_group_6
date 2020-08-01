from django.db import models
from django.contrib import admin


STATUSES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]


class GuestBook(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя автора записи')
    inbox = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Адрес электронной почты')
    record = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Запись')
    status = models.CharField(max_length=20, choices=STATUSES, default='active', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.record)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'record', 'inbox', 'created_at']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name', 'record', 'inbox', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']