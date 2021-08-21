from django.shortcuts import render
from django.http import HttpResponse


def soil(request):
    return render(request, 'Soil.html')


def index(request):
    return render(request, 'Soil.html')