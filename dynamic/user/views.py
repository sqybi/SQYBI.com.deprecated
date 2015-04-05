from django.shortcuts import render
import django.http


def user(request, user_name=None):
    return django.http.HttpResponseRedirect("/")