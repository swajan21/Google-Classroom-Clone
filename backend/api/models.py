from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    

    def __str__(self):
        return self.username
    


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classrooms_created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class ClassroomMember(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=(('student', 'Student'), ('teacher', 'Teacher')))
    joined_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    post_type = models.CharField(max_length=20, choices=(('announcement', 'Announcement'), ('assignment', 'Assignment')))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)