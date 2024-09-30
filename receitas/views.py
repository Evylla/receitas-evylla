from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Receita
from .forms import RecipeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import EmptyPage, Paginator

from random import randint


def home(request):

    receitas = Receita.objects.all().order_by('postado')

    p = Paginator(receitas, 10)

    lastpage = p.num_pages

    page_num = request.GET.get('page', 1)
    try:
        page = p.get_page(page_num)
    except EmptyPage:
        page = p.get_page(1)

    context = {
        'receitas': page,
        'last' : lastpage
        }

    return render(request, 'receitas/home.html', context)


def about(request):
    return render(request, 'receitas/about.html')


def newRecipe(request):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'message': messages
    }
    return render(request, 'receitas/receita_new.html', context)


    

def receita(request, pk):

    receita = Receita.objects.get(id=pk)

    ingredientes = receita.ingredientes
    ingrediente = ingredientes.split('\n')

    instruções = receita.instruções
    instrução = instruções.split('\n')

    context = {
        "receita": receita,
        'ingrediente':ingrediente,
        'instrução': instrução,
    }

    return render(request, "receitas/receita_detail.html", context)


def updateRecipe(request, pk):

    receita = Receita.objects.get(id=pk)
    form = RecipeForm(instance=receita)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'receitas/receita_update.html', context)


def deleteRecipe(request, pk):
    item = Receita.objects.get(id=pk)

    context = {
            'item':item,
        }

    if request.method == 'POST':
        item.delete()
        return redirect('home')

    
    return render(request, 'receitas/receita_delete.html', context)


def randomRecipe(request):

    count = Receita.objects.count()
    random_receita = Receita.objects.all()[randint(0, count - 1)] #single random object

    return HttpResponseRedirect(reverse("receita-detail", args=[random_receita.id]))

    
def pesquisa(request):
    if request.method == 'GET':
        receita = request.GET.get('receita')
        pesquisa = Receita.objects.filter(nome__contains=receita)
        return render(request, "receitas/home.html", {
            "receitas": pesquisa,
            "search": True,
        })
