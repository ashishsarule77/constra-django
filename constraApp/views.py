from django.shortcuts import render

# Create your views here.

def viewHome(request):
    resp = render(request,'constraApp/home.html')
    return resp
