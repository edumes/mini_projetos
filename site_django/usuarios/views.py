from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404

def cadastro(request):
    return HttpResponse('estou na pagina de cadastro')

def login(request):
    return HttpResponse('login')
