from django.contrib import admin
from .models import Author, Blog, Type, Comments

# Register your models here.

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Type)
admin.site.register(Comments)