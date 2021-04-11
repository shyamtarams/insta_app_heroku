from django.shortcuts import render
from django.http import HttpResponse

def indexfn(resquest):
    return HttpResponse("hello world  !")
    
def fn1(request):
    return HttpResponse("<h1>hello </h1>")

def fn2(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

