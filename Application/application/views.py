from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    streams = Stream.objects.all()
    students = Student.objects.all()
    context = {
        'streams':streams,
        'students':students
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = CreateStream(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
        return redirect('home')
    else:
        form = CreateStream()
    context = {
        'form':form,
    }
    return render(request, 'create_stream.html', context)


def create_student(request):
    if request.method == 'POST':
        form = CreateStudent(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
        return redirect('home')
    else:
        form = CreateStudent()
    context = {
        'form':form,
    }
    return render(request, 'create_student.html', context)


def student_deets(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student':student,
    }
    return render(request, 'student_details.html', context)


def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
       form = EditStudent(request.POST)
       if form.is_valid():
           edit = form.save(commit=False)
           edit.id = id
           edit.save()
       return redirect('home')
    else:
       form = EditStudent()

    context = {
        'form':form,
        'student':student,
    }
    return render(request, 'edit_student.html', context)


def all_students(request, id):
    students = Student.objects.filter(stream=id).all()
    context = {
        'students':students
    }
    return render(request, 'all_students.html', context)


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('home')