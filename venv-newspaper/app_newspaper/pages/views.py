from turtle import home
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name= "home.html"
    
class Error403(TemplateView):
    template_name = 'error.html'
