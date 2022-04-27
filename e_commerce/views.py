from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def home_page(request):
    context = {"title": "Pagina Principal",
               "content": "Bem vindo a pagina principal!"}
    return render(request, 'home_page/view.html', context)


def about(request):
    context = {"title": "Sobre nós",
               "content": "Bem vindo a sobre nós!"}
    return render(request, 'about/view.html', context)


def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {

        "title": "Página de contato",
        "content": "Bem-vindo a página de contato",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
        # print(request.POST)
        # print(request.POST.get('Nome_Completo'))
        # print(request.POST.get('email'))
        # print(request.POST.get('Mensagem'))
    return render(request, "contact/view.html", context)
