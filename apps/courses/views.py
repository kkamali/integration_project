from django.shortcuts import render, redirect, reverse
from . import models
from django.db.models import Count
import datetime

# Create your views here.
def index(request):
    courses = models.Course.objects.all()
    context = {
        'courses' : courses
    }
    return render(request, "courses/index.html", context)

def submit(request):
    name = request.POST['name']
    description = request.POST['description']
    time = datetime.datetime.now()
    query = models.Course(name = name, description = description)
    query.save()
    return redirect(reverse("courses:index"))

def question(request):
    request.session['course_id'] = request.POST['id']
    courses = models.Course.objects.all().get(pk = request.session['course_id'])
    context = {'courses' : courses}
    return render(request, "courses/delete.html", context)

def remove(request):
    models.Course.objects.all().get(pk = request.session['course_id']).delete()
    return redirect(reverse("courses:index"))

def user(request):
    courses = models.Course.objects.annotate(students=Count('users'))
    users = models.User.objects.all()
    context = {
        'courses' : courses,
        'users' : users
    }
    return render(request, "courses/users_course.html", context)

def add(request):
    models.Course.objects.add_student(request.POST['course'], request.POST['user'])
    return redirect(reverse("courses:index"))
