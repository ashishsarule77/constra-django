from django.urls import path
from .views import *


urlpatterns=[
    path('home/',viewHome,name='home'),
    path('hometwo/',view_home_two,name="hometwo"),
    path('about/',view_company_about,name='about'),
    path('people/',view_people,name="people"),
    path('testimonial/',view_testrimonial,name="testimonial"),

]