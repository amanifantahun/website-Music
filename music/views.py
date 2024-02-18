from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def home(request):

    return render(request, 'home.html',)


def about(request):
    return HttpResponse('about page')


def contact_page(request):
    return HttpResponse('cotact page')


def music(request):
    return HttpResponse('music page')

