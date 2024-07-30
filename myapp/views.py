from inspect import Parameter
from django.shortcuts import render,redirect
from .models import Todo
# ========================home funtion===================================

def home(request):
    return render(request,"home.html")
#========================todo funtion===================================


def todo(request):
    result=Todo.objects.all()
    completed_tasks=result.filter(is_completed=True)
    incompleted_tasks=result.filter(is_completed=False)
    
    
    Parameter={
        "todos":incompleted_tasks,
        "completed_tasks":completed_tasks,
        "name":"Laavi",
        
    
    }
    return render(request,"todo.html",Parameter)

# ========================add_todo funtion===================================



def add_todo(request):
    #template se data aa rha h
    if request.method=="POST":
        user_task=request.POST.get("task1")
        user_created_at=request.POST.get("created_at2")
        #saving that data in model
        new_todo=Todo(task=user_task,created_at=user_created_at)
        new_todo.save()
        is_completed=False  
        return redirect("todo")
    return render(request,"add_todo.html")


# ==============================delete===================================
def delete_todo(request,todo_id):
    remove=Todo.objects.get(id=todo_id)
    remove.delete()
    return redirect("todo")




# ========================update funtion===================================


def update_todo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    if request.method=="POST":
        
        user_task=request.POST.get("task1")
        user_created_at=request.POST.get("created_at2")
        todo.task=user_task
        todo.created_at=user_created_at
        todo.save()
        return redirect("todo")
        
   
    Parameter={
        "todos":todo,
       }
    return render(request,"update_todo.html",Parameter)
    
    return redirect("todo")


# ========================complete funtion===================================

def mark_complete(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.is_completed=True
    todo.save()
     
     
     
    return redirect("todo")
# ================function for profile page==================================

def profile(request):
    return render(request,"upload_profile_pic.html")
# ==================function for about page=================================
def about(request):
    return render(request,"about.html")

     
