import time
from django.shortcuts import render
from django.http import HttpResponse
from .models import *



def search(request):
    book = None
    return render(request, 'search.html', {
        'book': book,
    })


def theme(request):
    book = None
    return render(request, 'theme.html', {
        'book': book,
    })


def themes(request):
    book = None
    return render(request, 'themes.html', {
        'book': book,
    })



def clip(request):
    book = None
    return render(request, 'clip.html', {
        'book': book,
    })


def video(request):
    book = None
    return render(request, 'video.html', {
        'book': book,
    })



def interviews(request):
    book = None
    return render(request, 'interviews.html', {
        'book': book,
    })


def about(request):
    book = None
    return render(request, 'about.html', {
        'book': book,
    })


def interviews_home(request):
    book = None
    return render(request, 'home.html', {
        'book': book,
    })

