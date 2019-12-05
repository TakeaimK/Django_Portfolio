from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField()
    created_at = models.DateTimeField(auto_now=True)    #auto_now : 달력 클릭해서 바꿀 수 있음
    updated_at = models.DateTimeField(auto_now_add=True)    #auto_now_add : read only

    def __str__(self):
        return self.title