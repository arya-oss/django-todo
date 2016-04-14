from django.shortcuts import render
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import todo, tags

def index(req):
    return render(req, 'todo/index.html', {'title': 'Home'})

@login_required(login_url='/auth/login/')
def _add(req):
	HttpResponseRedirect('/todo/list/')

@login_required(login_url='/auth/login/')
def _show(req, id):
	if req.method == 'POST':
		return render(req, 'todo/show.html', {'title':'Show'})

@login_required(login_url='/auth/login/')
def list(req):
	in_tasks = todo.objects.filter(user=req.user, is_finished=False)
	com_tasks = todo.objects.filter(user=req.user, is_finished=True)
	return render(req, 'todo/list.html', {'title':'List','in_tasks':in_tasks,'com_tasks':com_tasks})
