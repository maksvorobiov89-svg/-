from django.contrib import admin
from .models import Post, Comment

# Кажемо Django показувати ці моделі в адмінці
admin.site.register(Post)
admin.site.register(Comment)