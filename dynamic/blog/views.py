from django.shortcuts import render, get_object_or_404
from django.http import Http404

from blog.models import Article

# Create your views here.
def index(request):
    articles = Article.objects.filter(is_shown = True).order_by("id")

    context = {
        "articles": articles,
    }

    return render(request, "blog/index.htm")

def article(request, article_id = None, article_slug = None):
    if article_id != None:
        article = get_object_or_404(Article, id = article_id)
    elif article_slug != None:
        article = get_object_or_404(Article, slug = article_slug)
    else:
        raise Http404

    context = {
        "article": article,
    }

    return render(request, "blog/article/show.htm", context)

