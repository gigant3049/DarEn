from rest_framework import serializers

from article.models import Article, Tag, Comment, SubArticle, Category, Author


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArticle
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        if obj.children:
            serializer = self.__class__(obj.children, many=True)
            return serializer.data
        return None

    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'category', 'tags', 'image', 'is_quote', 'slug', 'comments']
        extra_kwargs = {
            'slug': {'required': False},
        }