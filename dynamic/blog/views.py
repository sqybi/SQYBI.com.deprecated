from django.shortcuts import render, get_object_or_404
from django.http import Http404

from blog.models import BlogArticleItem
import helper.constants


def index(request, page=1):
    articles = BlogArticleItem.objects.filter(is_shown=True).order_by("create_time")[::-1]

    start_article = (page - 1) * 5;
    end_article = page * 5;

    context = {
        "title": "三千院大小姐的紫公馆 | SQYBI.com",
        "app": "blog",
        "alert_level": helper.constants.alert_level,
        "alert_message": helper.constants.alert_message,
        "all_articles": list(articles),
        "selected_articles": list(articles)[start_article:end_article],
    }

    return render(request, "blog/index.htm", context)


def article(request, article_id=None, article_slug=None):
    articles = BlogArticleItem.objects.filter(is_shown=True).order_by("id")[::-1]

    if article_id is not None:
        selected_article = get_object_or_404(BlogArticleItem, id=article_id)
    elif article_slug is not None:
        selected_article = get_object_or_404(BlogArticleItem, slug=article_slug)
    else:
        raise Http404

    context = {
        "title": selected_article.title + " | 三千院大小姐的紫公馆 | SQYBI.com",
        "app": "blog",
        "alert_level": helper.constants.alert_level,
        "alert_message": helper.constants.alert_message,
        "all_articles": list(articles),
        "selected_article": selected_article,
    }

    return render(request, "blog/article.htm", context)
