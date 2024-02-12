from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Страница MacaroonShop.")

def categories(request, cat):
    return HttpResponse(f"<h1>Привет</h1><p>{cat}</p")