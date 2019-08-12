from django.contrib import admin
from .models import CommentPub,Profile,Public

@admin.register(CommentPub,Profile,Public)
class Teste(admin.ModelAdmin):
    pass

# Register your models here.
