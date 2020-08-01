from django.db import models

class GuestBook(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя автора записи')
    inbox = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Адрес электронной почты')
    record = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Запись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.record)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'