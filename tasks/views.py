from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from .forms import TaskForm 

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='accounts/login/')
def taskApp(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/')

    else :
        taskItems = Tasks.objects.filter(author= request.user)
        form = TaskForm()
    return render(request, 'task_list.html', {'taskItems' : taskItems, 'form':form})


@login_required(login_url="{% url 'login' %}")
def del_task(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return redirect('/')

@login_required(login_url='accounts/login/')
def update_task(request, pk):
    task = Tasks.objects.get(id = pk)
    task.completed = not task.completed
    task.save()
    return redirect('/')