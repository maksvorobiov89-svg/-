from django import forms
from .models import Post, Comment

# Форма для створення поста
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Вказуємо, які поля людина має заповнити сама (дату Django поставить сам)
        fields = ('title', 'content', 'category', 'author')

# Форма для коментаря
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Коментатору треба вказати лише своє ім'я та текст
        fields = ('author_name', 'content')