from django.shortcuts import render
from .models import *


def search(request):
    book = None
    return render(
        request,
        "search.html",
        {
            "book": book,
        },
    )


def theme(request):
    book = None
    return render(
        request,
        "theme.html",
        {
            "book": book,
        },
    )


def themes(request):
    book = None
    return render(
        request,
        "themes.html",
        {
            "book": book,
        },
    )


def clip(request):
    book = None
    return render(
        request,
        "clip.html",
        {
            "book": book,
        },
    )


def video(request):
    book = None
    return render(
        request,
        "video.html",
        {
            "book": book,
        },
    )


def interviews(request):
    book = None
    return render(
        request,
        "interviews.html",
        {
            "book": book,
        },
    )



def about(request):
    p = Page.objects.filter(slug='about')[0]
    return render( request, "about.html", { "p": p, }, )


def interviews_home(request):
    p = Page.objects.filter(slug='home')[0]
    return render( request, "home.html", { "p": p, }, )

