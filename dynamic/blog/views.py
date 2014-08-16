from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Test View, this is the index page of SQYBI.com blog.");

def article(request, article_id = None, article_slug = None):
    if article_id != None:
        return HttpResponse("Request with article_id %s" % article_id)
    else:
        return HttpResponse("Request with article_slug %s" % article_slug)

