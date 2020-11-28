from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from .forms import TaskForm 
# Create your views here.
def taskApp(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else :
        taskItems = Tasks.objects.all()
        form = TaskForm()
    return render(request, 'task_list.html', {'taskItems' : taskItems, 'form':form})



def del_task(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return redirect('/')

def update_task(request, pk):
    task = Tasks.objects.get(id = pk)
    task.completed = not task.completed
    task.save()
    return redirect('/')