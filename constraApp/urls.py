from django.urls import path
from .views import *


urlpatterns=[
    path('home/',viewHome,name='home'),

]