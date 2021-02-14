from django.shortcuts import render, HttpResponse, redirect
from crud.models import Article, Author
from django.contrib import messages

# Create your views here.

# Show the las article created and the last Author Created


def home(request):
    articles = Article.objects.order_by('-created_at')[:1]
    authors = Author.objects.order_by('-created_at')[:1]
    return render(request, 'index.html', {'articles': articles, 'authors': authors})


def article_form_creation(request):
    return render(request, 'article_creation.html')


def article_creation(request):
    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        article = Article(
            title=title,
            content=content,
            public=public,)
        article.save()

       
        return redirect('articles_list')
    else:
        return HttpResponse("<h1>Error creating this article please try Again<h1>")


def article_form_update(request, pk):

    article = Article.objects.get(pk=pk)
    return render(request, 'article_update.html', {'article': article})


def article_update(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)

        article.title = request.POST['title']
        article.content = request.POST['content']
        article.public = request.POST['public']

        article.save()
        return redirect('articles_list')

    else:
        return HttpResponse(f"<h1>Error updating this Article</h1>")


def articles_list(request):
    # Read all data articles from database without sort the data
    articles = Article.objects.all()

    return render(request, 'articles_list.html', {'articles': articles})


def article_delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles_list')


def author_form_creation(request):
    return render(request, 'author_creation.html')


def author_creation(request):
    if request.method == 'POST':
        author = Author(
            nombre=request.POST['nombre'],
            email=request.POST['email'],)
        author.save()
        return redirect('authors_list')
    else:
        return HttpResponse("<h1>Error creating this article please try Again<h1>")


def author_form_update(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'author_update.html', {'author': author})


def author_update(request, pk):
    if request.method == 'POST':
        author = Author.objects.get(pk=pk)

        author.nombre = request.POST['nombre']
        author.email = request.POST['email']
        author.save()
        return redirect('authors_list')

    else:
        return HttpResponse(f"<h1>Error al actualizar el artículo.</h1>")
   


def authors_list(request):
    # Read all data Authors from database without sort the data
    authors = Author.objects.all()

    return render(request, 'authors_list.html', {'authors': authors})


def author_delete(request, pk):
    author = Author.objects.get(pk=pk)
    author.delete()
    return redirect('authors_list')
