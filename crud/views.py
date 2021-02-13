from django.shortcuts import render, HttpResponse, redirect
from crud.models import Article, Author

# Create your views here.


def home(request):
    return render(request, 'index.html')


def article_creation(request):
    return render(request, 'article_creation.html')


def article_uptdate(request):
    return render(request, 'article_update.html')


def articles_list(request):
    return render(request, 'articles_list.html')


def author_creation(request):
    return render(request, 'author_creation.html')


def author_uptdate(request):
    return render(request, 'author_update.html')


def authors_list(request):
    return render(request, 'authors_list.html')
