from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import consumerForm, loginForm,todoForm,store_editTodoForm
from django.contrib import messages
from django.urls import reverse
from . import models
from .decorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def mainView(request):
    context = {}
    return render(request,'TODO_web/main.html',context)

@authorise
def loginView(request):

    if request.user.is_authenticated:
        print("authenticated")
    else:
        print('not autheticated')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password = password)
        if user is not None:
            login(request,user)
            
            redirect_url = reverse('home',kwargs={'pk':user.id})
            return redirect(redirect_url)
        else:
            messages.info(request,"Username or Password are incorrect")

    form = loginForm()
    context = {'form':form}
    return render(request,'TODO_web/loginPage.html',context)

def register(request):

    if request.method == 'POST':
        form = consumerForm(request.POST)
        if form.is_valid:
            user = form.save()
            

            return redirect('login')


    form = consumerForm()

    
    context = {'form':form}
    
    return render(request,'TODO_web/registerPage.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def homeView(request,pk):

    if request.method == 'POST':
    
        newTask = todoForm(request.POST)
        
        # newTask.cleaned_data.update(['consumer',user])
        
        if newTask.is_valid():
    
            newTask.save()


    user = models.consumers.objects.get(id=pk)
    tasks = user.todo_set.all()
    task_field = todoForm(initial={'consumer':user})

    store_edit_field = {}
    for task in tasks:
        upd_val = {task.id:store_editTodoForm(initial={'consumer':user,'task':task})}
        store_edit_field.update(upd_val)
        # store_edit_field.append(store_editTodoForm(initial={'consumer':user,'task':task}))
    # print('*****************************************************')
    # # print(type(store_edit_field))
    # print("#################################################")
    # for task_f in store_edit_field:
    #     print(type(task_f.task))
    #     # print(task_f.task.id)
    
    # print("#################################################")
    # print(store_edit_field)

    

    

    context = {'task_field':task_field,'tasks':tasks,'store_edit_field':store_edit_field}

    return render(request,'TODO_web/home.html',context)


def deleteTask(request,taskID):
    task = models.Todo.objects.get(id=taskID)
    consumer = task.consumer
    task.delete()
    redirectTo = reverse('home',kwargs={'pk':consumer.id})
    return redirect(redirectTo)


def updateTask(request,taskID):
    task_detail = models.Todo.objects.get(id=taskID)
    consumer = task_detail.consumer
    print('task : ',task_detail)
    

    if request.method == "POST":
        taskForm = store_editTodoForm(request.POST, instance=task_detail)
        print('##########################################')
        
        if taskForm.is_valid():
            taskForm.save()
        else:
            print('##########################################')
            print(taskForm.cleaned_data.get('consumer'))
            print(taskForm.cleaned_data.get('task'))
            # print(taskForm.cleaned_data.consumer)
            print("#################################################")
            
    redirectTo = reverse('home',kwargs={'pk':consumer.id})
    return redirect(redirectTo)
        
