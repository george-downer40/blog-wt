from django.shortcuts import render
from django.http import HttpResponse

#views

def my_blog(request):
    return HttpResponse('Hello, Blog!')