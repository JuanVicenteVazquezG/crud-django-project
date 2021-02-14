"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Views import views

from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.home, name="home"),
    path('articles/', views.articles_list, name="articles_list"),
    path('article/create/', views.article_creation, name="article_creation"),
    path('article/formcreate/', views.article_form_creation, name="article_form_creation"),
    path('article/update/<int:pk>', views.article_update, name="article_update"),
    path('article/formupdate/<int:pk>', views.article_form_update, name="article_form_update"),
    path('article/delete/<int:pk>', views.article_delete, name="article_delete"),
    path('authors/', views.authors_list, name="authors_list"),
    path('author/formcreation', views.author_form_creation, name="author_form_creation"),
    path('author/create/', views.author_creation, name="author_creation"),
    path('author/update/', views.author_uptdate, name="author_uptdate"),
    path('', views.home, name="home"),
]
