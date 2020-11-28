from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model) :
    title = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add = True)
    completed = models.BooleanField(default= False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.title