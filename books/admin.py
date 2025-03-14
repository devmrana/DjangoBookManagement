from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'genre')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('genre', 'published_date')

admin.site.register(Book, BookAdmin)
