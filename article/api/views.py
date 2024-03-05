from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from article.models import Article
from .serializers import ArticleSerializer


@api_view(['GET'])
def article_list(request):
    qs = Article.objects.all()
    serializer = ArticleSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, slug):
    qs = Article.objects.filter(slug=slug)
    serializer = ArticleSerializer(qs)
    obj = get_object_or_404(Article, slug=slug)
    if request.method == 'GET':
        serializer = ArticleSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            obj = get_object_or_404(Article, slug=serializer.data.get('slug'))
            serializer = ArticleSerializer(obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {
            'success': False,
            'message': "Something went wrong",
            'errors': serializer.errors
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    qs = Article.objects.all()
    serializer = ArticleSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        obj = get_object_or_404(Article, slug=serializer.data.get('slug'))
        serializer = ArticleSerializer(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    data = {
        'success': False,
        'message': "Something went wrong",
        'errors': serializer.errors
    }
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


