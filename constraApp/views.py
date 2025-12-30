from django.shortcuts import render

# Create your views here.

def viewHome(request):
    resp = render(request,'constraApp/home.html')
    return resp


def view_home_two(request):
    resp = render(request,"constraApp/home_two.html")
    return resp

def view_company_about(request):
    resp = render(request,"constraApp/about.html")
    return resp

def view_people(request):
    resp = render(request,"constraApp/ourpeople.html")
    return resp

def view_testrimonial(request):
    resp = render(request,"constraApp/testimonial.html")
    return resp