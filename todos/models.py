from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    deadline = models.DateField(blank=False, null=False)
    finished_at = models.DateField(null=True)
