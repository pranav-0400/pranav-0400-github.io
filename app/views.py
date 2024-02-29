from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Items
from django.shortcuts import get_object_or_404  

# Create your views here.


def home(request):
    if request.method == 'POST':
        task_text = request.POST.get('task_text')
        Items.objects.create(task=task_text)
        return redirect('home')

    
    
    
    items = Items.objects.all()   # Imp to remember

    # Pass the items to the template context
    context = {'items': items}
    return render(request,'app/base.html', context)


def delete_task(request, task_id):
    if request.method == 'POST':
        task_to_delete = Items.objects.get(id=task_id)
        task_to_delete.delete()

    # Redirect back to the home view after deleting the task
    return redirect('home')

def edit_task(request, task_id):
    if request.method == 'POST':
        edited_text = request.POST.get('edited_text')
        task_to_edit = get_object_or_404(Items, id=task_id)
        task_to_edit.task = edited_text
        task_to_edit.save()

    return redirect('home')
    