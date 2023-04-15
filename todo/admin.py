from django.contrib import admin

# Register your models here.

# Register your models  with class TodoItemAdmin(admin.ModelAdmin):

#     list_display = ('title', 'content', 'completed', 'image')

from .models import TodoItem
@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'completed', 'image')
