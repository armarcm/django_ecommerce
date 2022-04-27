from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    context = {"title": "Pagina Principal",
               "content": "Bem vindo a pagina principal!"}
    return render(request, 'home_page/view.html', context)


def about(request):
    context = {"title": "Sobre nós",
               "content": "Bem vindo a sobre nós!"}
    return render(request, 'about/view.html', context)


def contact(request):
    context = {"title": "Pagina de contato",
               "content": "Bem vindo a pagina de contato!"}
    return render(request, 'contact/view.html', context)
