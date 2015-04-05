from django.shortcuts import render, get_object_or_404
from django.http import Http404

from blog.models import BlogArticleItem
import helper.constants


def index(request, page=1):
    recent_articles = list(
        BlogArticleItem.objects.filter(is_shown=True).order_by("id").reverse()[:helper.constants.blog_article_per_page])

    start_article = (page - 1) * helper.constants.blog_article_per_page;
    end_article = page * helper.constants.blog_article_per_page;

    total_article_count = BlogArticleItem.objects.filter(is_shown=True).count()

    total_page_count = (
                       total_article_count - 1 + helper.constants.blog_article_per_page) / helper.constants.blog_article_per_page

    selected_articles = list(
        BlogArticleItem.objects.filter(is_shown=True).order_by("id").reverse()[start_article:end_article])

    context = {
        "title": helper.constants.blog_title + " | SQYBI.com",
        "app": "blog",
        "alert_level": helper.constants.alert_level,
        "alert_message": helper.constants.alert_message,
        "recent_articles": recent_articles,
        "selected_articles": selected_articles,
        "prev_page": None if page <= 1 else str(page - 1),
        "next_page": None if page >= total_page_count else str(page + 1),
    }

    return render(request, "blog/index.html", context)


def article(request, article_id=None, article_slug=None):
    recent_articles = list(
        BlogArticleItem.objects.filter(is_shown=True).order_by("id").reverse()[:helper.constants.blog_article_per_page])

    if article_id is not None:
        selected_article = get_object_or_404(BlogArticleItem, id=article_id)
    elif article_slug is not None:
        selected_article = get_object_or_404(BlogArticleItem, slug=article_slug)
    else:
        raise Http404

    previous_article = BlogArticleItem.objects.filter(id__lt=selected_article.id, is_shown=True).order_by(
        "id").reverse().first()
    next_article = BlogArticleItem.objects.filter(id__gt=selected_article.id, is_shown=True).order_by("id").first()

    context = {
        "title": selected_article.title + " | " + helper.constants.blog_title + " | SQYBI.com",
        "app": "blog",
        "alert_level": helper.constants.alert_level,
        "alert_message": helper.constants.alert_message,
        "recent_articles": recent_articles,
        "selected_article": selected_article,
        "prev_article": previous_article,
        "next_article": next_article,
    }

    return render(request, "blog/article.html", context)
