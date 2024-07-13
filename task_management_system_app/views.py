from django.shortcuts import render, redirect, HttpResponse
from .models import User, Task
from .forms import TaskForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import xlwt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = int(request.POST['mobile'])
        new_user = User(name = name, email = email, mobile = mobile)
        new_user.save()
        return HttpResponse('User Added Successfully...')

    elif request.method == 'GET':
        return render(request, 'add_user.html')
    else:
        return HttpResponse('An Exception Occured! User has not been added')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_task_lists')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def all_user_lists(request):
    user_list = User.objects.all().order_by('id')  
    paginator = Paginator(user_list, 5) 
    page = request.GET.get('page')
    
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    context = {
        'users': users
    }
    
    return render(request, 'all_user_lists.html', context)

def all_task_lists(request):
    task_list = Task.objects.all().order_by('id')
    paginator = Paginator(task_list, 5) 
    page = request.GET.get('page')
    
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    context = {
        'tasks' : tasks
    }
    return render(request, 'all_task_lists.html', context)

def export_users_tasks_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users_tasks.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    row_num = 0
    columns = ['Name', 'Email', 'Mobile']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    rows = User.objects.all().values_list('name', 'email', 'mobile')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num])

    ws = wb.add_sheet('Tasks')
    row_num = 0
    columns = ['User', 'Detail', 'Type']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    rows = Task.objects.all().values_list('user__name', 'detail', 'type')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num])

    wb.save(response)
    return response