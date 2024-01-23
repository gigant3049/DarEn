from django.shortcuts import render
from article.models import Article


def article_archive(request):

    ctx = {

    }
    return render(request, 'article/archive.html', ctx)


def article_category(request):

    ctx = {

    }
    return render(request, 'article/category.html', ctx)


def article_detail(request):

    ctx = {

    }
    return render(request, 'article/single-blog.html', ctx)
