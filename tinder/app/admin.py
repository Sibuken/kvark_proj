from django.contrib import admin
from .models import MyUser

@admin.register(MyUser)
class AuthorAdmin(admin.ModelAdmin):
    pass
