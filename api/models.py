# api/models.py
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Book(models.Model):
    STATUS_CHOICES = (
        ('reading', 'Currently Reading'),
        ('completed', 'Completed'),
        ('want_to_read', 'Want to Read'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tags = TaggableManager(blank=True)
    isbn = models.CharField(max_length=13, db_index=True, blank=True)
    total_pages = models.PositiveIntegerField(null=True, blank=True)
    current_page = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='want_to_read'
    )
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def progress_percentage(self):
        if self.total_pages and self.total_pages > 0:
            return round((self.current_page / self.total_pages) * 100)
        return 0
    
    class Meta:
        ordering = ['-date_added']
        unique_together = ['user', 'title', 'author'] 
        verbose_name = 'Book'

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['book', 'user']
        ordering = ['-created_at']