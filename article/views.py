from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from article.forms import CommentForm
from article.models import Article, SubArticle, Category, Tag, Author, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def article_archive(request):
    articles = Article.objects.order_by('-id')
    last_three_articles = articles[len(articles)-4:]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    query = request.GET.get('q')
    articles_per_page = 8
    paginator = Paginator(articles, articles_per_page)
    page = request.GET.get('page')

    try:
        paginated_articles = paginator.page(page)
    except PageNotAnInteger:
        paginated_articles = paginator.page(1)
    except EmptyPage:
        paginated_articles = paginator.page(paginator.num_pages)

    if query:
        paginated_articles = articles.filter(
            Q(title__icontains=query)|Q(content__icontains=query)
        )

    ctx = {
        'articles': paginated_articles,
        'paginated_articles': paginated_articles,
        'last_three_articles': last_three_articles,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'article/archive.html', ctx)


def article_category(request):
    articles = Article.objects.order_by('-id')
    last_three_articles = articles[:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')

    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if cat:
        articles = articles.filter(category__title__exact=cat)

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
        'articles': articles,
        'last_three_articles': last_three_articles,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'article/category.html', ctx)


def article_detail(request, slug):
    form = CommentForm()
    object_l = Article.objects.order_by('-id')[:3]
    article = get_object_or_404(Article, slug=slug)
    subarticles = SubArticle.objects.filter(article=article)
    comments = Comment.objects.filter(article_id=article.id, top_level_comment_id__isnull=True).order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cid = request.GET.get('cid')

    if request.method == "POST":
        comment = CommentForm(request.POST, request.FILES)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.article = article
            comment.parent_id = cid
            comment.save()
            messages.success(request, 'Comment sent successfully!')
            return redirect(".")

    ctx = {
        'last_three': object_l,
        'article': article,
        'subarticles': subarticles,
        'comment_form': form,
        'comments': comments,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'article/single-blog.html', ctx)
