from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app2(request):
    return HttpResponse('<h1>This is first app2 application</h1>')

def second_app2(request):
    return HttpResponse('<h1><marquee> this is second app2 </marquee></h1>')