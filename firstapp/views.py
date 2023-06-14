from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    count=["first","second","third","fourth"]
    developer="Sanjeev dhatterwal"
    context={"counts":count,
    "develop":developer,
    "show":False
    }
    response=render(request,'firstapp/index.html',context)
    # response =HttpResponse("Hello world")
    return response
def hello(request):
    response=render(request,'firstapp/hello.html')
    return response