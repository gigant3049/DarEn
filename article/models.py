from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify


class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    content = RichTextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='media/articles', blank=True, null=True)
    slug = models.SlugField(unique=False, editable=True)
    tags = models.ManyToManyField(Tag)
    is_quote = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='SubArticles')
    content = RichTextField(null=True, blank=True)
    is_quote = models.BooleanField(default=False)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = RichTextField()
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/articles', null=True, blank=True)

    @property
    def children(self):
        if not self.parent:
            return Comment.objects.filter(top_level_comment_id=self.id)
        return None

    def __str__(self):
        return self.name


def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(f"{instance.title}-{timezone.now().date()}")
        instance.slug += f"-{int(timezone.now().timestamp())}"


pre_save.connect(article_pre_save, sender=Article)


def pre_save_comments(sender, instance, *args, **kwargs):
    if instance.parent:
        if instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
        else:
            instance.top_level_comment_id = instance.parent.id


pre_save.connect(pre_save_comments, sender=Comment)