from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse(req, 'You wanna go to Auth home ?')

def login(req):
    return render(req, 'auth/login.html', {'title':'Auth | Login', 'author': 'Rajmani Arya'})
