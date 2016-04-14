from django.shortcuts import render
# Create your views here.
from django.contrib.auth.decorators import login_required

def index(req):
    return render(req, 'todo/index.html', {'title': 'Home'})

@login_required(login_url='/auth/login/')
def list(req):
    return render(req, 'todo/list.html', { 'title':'List', 'author': 'Rajmani Arya'})
