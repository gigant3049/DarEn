from django.contrib import admin

from .models import (
    Article,
    Comment,
    Category,
    Tag,
    Author,
    SubArticle
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


# class SubArticleInline(admin.StackedInline):
#     model = SubArticle
#     extra = 1
class SubArticleInlineAdmin(admin.StackedInline):
    model = SubArticle
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (SubArticleInlineAdmin, )
    list_display = ('id', 'title', 'image')
    readonly_fields = ('slug', 'created_date')
    search_fields = ('slug', 'title')
    list_filter = ('category', 'tags')
    autocomplete_fields = ('author', )

    def is_quote_checkbox(self, obj):
        return obj.is_quote

    is_quote_checkbox.boolean = True  # Display as a checkbox in the admin list view
    is_quote_checkbox.short_description = 'Is Quote'  # Set a custom header for the column


# @admin.register(SubArticle)
# class SubArticleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'article', 'is_quote_checkbox')
#     search_fields = ('title', 'article__title')  # assuming article is a ForeignKey field in SubArticle
#
#     def is_quote_checkbox(self, obj):
#         return obj.is_quote
#
#     is_quote_checkbox.boolean = True  # Display as a checkbox in the admin list view
#     is_quote_checkbox.short_description = 'Is Quote'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'children', 'name', 'email', 'content', 'created_date')
    readonly_fields = ('created_date', )
    search_fields = ('name', 'email')
