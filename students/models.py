from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id = models.CharField(max_length = 20, unique = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    course = models.CharField(max_length=100)
    trainer = models.ForeignKey(User, on_delete = models.CASCADE,related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id


