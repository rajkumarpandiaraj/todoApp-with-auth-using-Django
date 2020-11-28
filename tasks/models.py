from django.db import models

# Create your models here.
class Tasks(models.Model) :
    title = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add = True)
    completed = models.BooleanField(default= False)

    def __str__(self):
        return self.title