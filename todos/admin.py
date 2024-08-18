from django.contrib import admin
from . models import Todo




@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at",]
    search_fields = ["title", "created_at"]
    list_filter = ["created_at",]
    date_hierarchy = "created_at"
  