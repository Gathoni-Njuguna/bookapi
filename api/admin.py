# api/admin.py
from django.contrib import admin
from .models import Book, Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'user', 'status', 'date_added']
    list_filter = ['status', 'date_added']
    search_fields = ['title', 'author', 'user__username']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['book__title', 'user__username']