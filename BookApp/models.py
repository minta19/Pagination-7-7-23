from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=355)
    author=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title