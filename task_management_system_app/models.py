from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'User'

class Task(models.Model):
    PENDING = 'Pending'
    DONE = 'Done'
    TASK_TYPES = [
        (PENDING, 'Pending'),
        (DONE, 'Done')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.TextField(max_length=50)
    type = models.CharField(max_length=30, choices=TASK_TYPES, default=PENDING)

    def __str__(self):
        return f"{self.detail} - {self.type}"
    
    class Meta:
        db_table = 'Task'
