from django.db import models

# Create your models here.


class Task(models.Model):
    """Task Model Representation."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title