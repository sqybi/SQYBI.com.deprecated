from django.shortcuts import render, get_object_or_404
from django.http import Http404

from blog.models import BlogArticleItem


def index(request, page=1):
    articles = BlogArticleItem.objects.filter(is_shown=True).order_by("id")[::-1]

    start_article = (page - 1) * 5;
    end_article = page * 5;

    context = {
        "articles": list(articles),
        "selected_articles": list(articles)[start_article:end_article],
        "app": "blog",
    }

    return render(request, "blog/index.htm", context)


def article(request, article_id=None, article_slug=None):
    articles = BlogArticleItem.objects.filter(is_shown=True).order_by("id")[::-1]

    if article_id is not None:
        article_object = get_object_or_404(BlogArticleItem, id=article_id)
    elif article_slug is not None:
        article_object = get_object_or_404(BlogArticleItem, slug=article_slug)
    else:
        raise Http404

    context = {
        "articles": list(articles),
        "article": article_object,
        "app": "blog",
    }

    return render(request, "blog/article.htm", context)
