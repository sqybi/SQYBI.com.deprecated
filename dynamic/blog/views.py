from django.shortcuts import render, get_object_or_404
from django.http import Http404

from blog.models import BlogArticleItem
import helper.constants


def index(request, page=1):
    articles = BlogArticleItem.objects.filter(is_shown=True).order_by("create_time")[::-1]

    start_article = (page - 1) * helper.constants.blog_article_per_page;
    end_article = page * helper.constants.blog_article_per_page;

    total_page = (len(articles) - 1 + helper.constants.blog_article_per_page) / helper.constants.blog_article_per_page

    context = {
        "title": helper.constants.blog_title + " | SQYBI.com",
        "app": "blog",
        "alert_level": helper.constants.alert_level,
        "alert_message": helper.constants.alert_message,
        "all_articles": list(articles),
        "selected_articles": list(articles)[start_article:end_article],
        "prev_page": None if page <= 1 else str(page - 1),
        "next_page": None if page >= total_page else str(page + 1),
    }

    return render(request, "blog/index.html", context)


def article(request, article_id=None, article_slug=None):
    articles = BlogArticleItem.objects.filter(is_shown=True).order_by("id")[::-1]

    if article_id is not None:
        selected_article = get_object_or_404(BlogArticleItem, id=article_id)
    elif article_slug is not None:
        selected_article = get_object_or_404(BlogArticleItem, slug=article_slug)
    else:
        raise Http404

    context = {
        "title": selected_article.title + " | " + helper.constants.blog_title + " | SQYBI.com",
        "app": "blog",
        "alert_level": helper.constants.alert_level,
        "alert_message": helper.constants.alert_message,
        "all_articles": list(articles),
        "selected_article": selected_article,
    }

    return render(request, "blog/article.html", context)
