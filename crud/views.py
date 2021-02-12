from django.shortcuts import render, HttpResponse as http

# Create your views here.

def home(request):
    return http('<h1>At the beguining all was darkness!</h1>')

