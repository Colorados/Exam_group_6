from django.contrib import admin
from guest_book_app.models import GuestBook, ArticleAdmin

admin.site.register(GuestBook, ArticleAdmin)