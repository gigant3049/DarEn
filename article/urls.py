from django.urls import path
from .views import article_detail, article_archive, article_category

app_name = 'article'

urlpatterns = [
    path('archive/', article_archive, name='archive'),
    path('category/', article_category, name='category'),
    path('detail/<slug:slug>/', article_detail, name='detail')
]
