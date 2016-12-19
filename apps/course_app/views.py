from django.shortcuts import render, redirect
from .models import Courses

# Create your views here.
def index(request):
	context = { 'courses': Courses.objects.all() }
	return render(request, 'course_app/index.html', context)

def createcourse(request):
	Courses.objects.create(name=request.POST['name'], description=request.POST['description'])
	courses = Courses.objects.all()
	print courses
	return redirect('/')

def removecourse(request, id):
	context = { 'course': Courses.objects.get(id=id) }
	print "in remove course"
	return render(request, 'course_app/destroy.html', context)

def deletecourse(request, id):
	Courses.objects.get(id=id).delete()
	return redirect('/')