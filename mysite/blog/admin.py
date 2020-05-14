from django.contrib import admin
from .models import Post

#rejestracja modelu, by był widoczny w panelu admina
admin.site.register(Post)