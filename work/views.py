from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse(req, 'You wanna go to todos home ?')

def list(req):
    return render(req, 'todo/list.html', { 'title':'ToDos | List', 'author': 'Rajmani Arya'})
