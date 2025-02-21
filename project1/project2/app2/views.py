from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_msg(request):
    data ="ok done u have got"
    data1='no dude'
    return HttpResponse(data)

