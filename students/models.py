from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    COURSE_CHOICES = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('C++', 'C++'),
        ('C#', 'C#'),
        ('JavaScript', 'JavaScript'),
        ('Django', 'Django'),
        ('Flask', 'Flask'),
        ('React JS', 'React JS'),
        ('Node JS', 'Node JS'),
        ('Full Stack', 'Full Stack Development'),
        ('MERN Stack', 'MERN Stack'),
        ('MEAN Stack', 'MEAN Stack'),
        ('HTML & CSS', 'HTML & CSS'),
        ('SQL', 'SQL'),
        ('MySQL', 'MySQL'),
        ('PostgreSQL', 'PostgreSQL'),
        ('Data Science', 'Data Science'),
        ('Machine Learning', 'Machine Learning'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Generative AI', 'Generative AI'),
        ('Data Analytics', 'Data Analytics'),
        ('Cloud Computing', 'Cloud Computing'),
        ('AWS', 'AWS'),
        ('DevOps', 'DevOps'),
        ('Cyber Security', 'Cyber Security'),
        ('Software Testing', 'Software Testing'),
        ('Android Development', 'Android Development'),
        ('iOS Development', 'iOS Development'),
        ('Data Structures', 'Data Structures & Algorithms'),
    ]
    student_id = models.CharField(max_length = 20, unique = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    trainer = models.ForeignKey(User, on_delete = models.CASCADE,related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id


