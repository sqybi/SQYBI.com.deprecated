from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Article

# Create your views here.
def index(request):
    return HttpResponse("Test View, this is the index page of SQYBI.com blog.");

def article(request, article_id = None, article_slug = None):
    if article_id != None:
        article = Article.objects.get(id=article_id)
    elif article_slug != None:
        article = Article.objects.get(slug=article_slug)
    else:
        return HttpResponse("Error request!")
    return HttpResponse("<h3>%s</h3><p>%s</p>" % (article.title, article.html_content))

