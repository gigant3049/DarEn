from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from article.models import Article, Tag, Category
from main.forms import ContactForm


def main_index(request):
    articles = Article.objects.order_by('-id')
    lst_three = articles[:3]
    tag = request.GET.get('tag')
    category = request.GET.get('category')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    articles_per_page = 6
    paginator = Paginator(articles, articles_per_page)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    ctx = {
        'lst_three': lst_three,
        'articles': articles,
        'category': category,
        'tag': tag,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'main/index.html', ctx)


def contact(request):
    form = None
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully!')
            return redirect('main:contact')

    ctx = {
        "form": form,
    }
    return render(request, 'main/contact.html', ctx)
