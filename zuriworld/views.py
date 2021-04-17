from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h3>Hello world!! This is my first application. All thanks to the Zuri team</h3>')
