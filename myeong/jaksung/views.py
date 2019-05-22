from django.shortcuts import render, redirect
from .models import Dong
from .models import Bang


def home(request):
    dongs = Dong.objects
    return render(request, 'home.html', {'dongs' : dongs})


def submit(request):
    d = Dong()
    d.message = request.GET['a']
    d.writer = request.GET['b']
    d.date = request.GET['c']
    d.save()
    return redirect('/')


def reple(request):
    e = Bang()
    e.message = request.GET['f']
    e.writer = request.GET['g']
    e.date = request.GET['h']
    e.save()
    return redirect('/')