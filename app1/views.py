from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app1(request):
    return HttpResponse('<h3>This is first app1 application</h3>')


def second_app1(request):
    return HttpResponse('<h1><button> This is second app1 apllication</button></h1>')