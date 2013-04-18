#-*- coding: utf-8 -*-
# Create your views here.

#from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
