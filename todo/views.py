# todo/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDo

def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = ToDo.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'todo/add.html')

def update(request, id):
    todo = get_object_or_404(ToDo, id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('index')
    return render(request, 'todo/update.html', {'todo': todo})

def delete(request, id):
    todo = get_object_or_404(ToDo, id=id)
    todo.delete()
    return redirect('index')
