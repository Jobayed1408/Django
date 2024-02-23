from django.shortcuts import render, redirect
from book.forms import TaskForm
from book.models import TaskModel
# Create your views here.
def home(request):
    return render(request, 'store_book.html')

def store_book(request):
    if request.method == 'POST':
        book = TaskForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('show_book')
    
    else:
        book = TaskForm() 
     
    return render(request, 'store_book.html', {'form':book}) 

def show_book(request):
    book = TaskModel.objects.all()
    # print(book)
    return render(request, 'show_book.html', {'data':book})

def edit_task(request, id):
    book = TaskModel.objects.get(pk = id) 
    form = TaskForm(instance=book) 
    if request.method == 'POST':
        book = TaskForm(request.POST, instance=book)
        if book.is_valid():
            book.save()
            return redirect('show_book')
    else:
        book = TaskForm() 
        
    return render(request, 'store_book.html', {'form':form}) 

def delete_task(request, id):
    book = TaskModel.objects.get(pk = id).delete()  
    return redirect('show_book')

def complete(request, id):
    book = TaskModel.objects.get(pk = id)
    TaskModel.objects.get(pk = id).delete()   
    return render(request, 'complete_task.html', {'book':book}) 



