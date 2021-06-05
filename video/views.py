import time
from django.shortcuts import render
from django.http import HttpResponse
from .models import *



def search(request):
    #book = Book.objects.all()
    return render(request, 'tag.html, {
        'book': book,
    })


def theme(request):
    #book = Book.objects.all()
    return render(request, 'theme.html, {
        'book': book,
    })


def themes(request):
    #book = Book.objects.all()
    return render(request, 'themes.html, {
        'book': book,
    })



def clip(request):
    #book = Book.objects.all()
    return render(request, 'clip.html, {
        'book': book,
    })


def video(request):
    #book = Book.objects.all()
    return render(request, 'video.html, {
        'book': book,
    })



def interviews(request):
    #book = Book.objects.all()
    return render(request, 'interviews.html, {
        'book': book,
    })


def about(request):
    #book = Book.objects.all()
    return render(request, 'about.html, {
        'book': book,
    })


def home(request):
    #book = Book.objects.all()
    return render(request, 'home.html, {
        'book': book,
    })

