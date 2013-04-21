#-*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def co(request):
    return render(request, 'co.html', {})

def manager(request):
    return render(request, 'manager.html', {})

def control(request):
    if request.is_ajax():
        if request.POST.get("id"):
            id = int(request.POST.get("id"))
            if id == 0:
                view = 'scan.html'
            elif id == 1:
                view = 'visu.html'
            elif id == 2:
                view = 'profil.html'
            elif id == 3:
                view = 'disconnect.html'
            else:
                view = 'error.html'
            return render_to_response(view, {})
        return HttpResponse("error POST" +request.POST.get("id")+request.method)
    return HttpResponse("error AJAX")