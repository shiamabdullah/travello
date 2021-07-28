from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#     return HttpResponse("Hello World")

def index(request):
    return render(request,'index.html',{'name':'Shiam'})

def add(request):
    
    val1= int(request.GET['num1'])
    val2= int(request.GET['num2'])
    res= int(val1+val2)


    return render(request,'result.html',{'answer':res})

def mul(request):
    al1= int(request.POST['a1'])
    al2= int(request.POST['a2'])
    resa= int(al1*al2)
    return render(request,'mulresult.html',{'answer':resa})
