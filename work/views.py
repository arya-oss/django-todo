from django.shortcuts import render
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import todo, tags
from .forms import WorkAddForm, TagsForm
from django.contrib.auth.models import User
from django.contrib import messages

def index(req):
    return render(req, 'todo/index.html', {'title': 'Home'})

@login_required(login_url='/auth/login/')
def _add(req):
    if req.method == "POST":
        work_form = WorkAddForm(data=req.POST)
        if work_form.is_valid():
            work_form.save(commit=False)
            work_form.user = User.objects.get(username=req.user.username)
            work_form.save()
            messages.info(req, 'Task Added !')
        else:
            messages.info(req, 'Invalid Task !')
            print work_form.errors
    return HttpResponseRedirect('/todo/list/')

@login_required(login_url='/auth/login/')
def _show(req, id):
	return render(req, 'todo/show.html', {'title':'Show'})

@login_required(login_url='/auth/login/')
def list(req):
    work_form = WorkAddForm()
    in_tasks = todo.objects.filter(user=req.user, is_finished=False)
    com_tasks = todo.objects.filter(user=req.user, is_finished=True)
    return render(req, 'todo/list.html', {'title':'List','work_form':work_form,'in_tasks':in_tasks,'com_tasks':com_tasks})
