from __future__ import unicode_literals
from django.db import models
from ..loginregister.models import User

# Create your models here.
class CourseManager(models.Manager):
    def add_student(self, course, user):
        course = self.get(id = course)
        student = User.objects.get(id = user)
        course.users.add(user)
        course.save()

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    users = models.ManyToManyField('loginregister.User', related_name = 'courses')
    objects = CourseManager()
