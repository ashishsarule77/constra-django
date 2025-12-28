from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_home(request):
    resp = HttpResponse("<h1> heyy Ahish </h1>")
    return resp