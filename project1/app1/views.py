from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_msg(request):
    data = "hello django"
    data1= "Hello world"
    return HttpResponse(data)