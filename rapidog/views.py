from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rapidog.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def produtos(request):
    alimentacao = Produto.objects.filter(disponivel=True, categoria='alimentacao').order_by('-id')[:5]
    higiene = Produto.objects.filter(disponivel=True, categoria='higiene').order_by('-id')[:5]
    brinquedos = Produto.objects.filter(disponivel=True, categoria='brinquedos').order_by('-id')[:5]

    context = {
        'alimentacao': alimentacao,
        'higiene': higiene,
        'brinquedos': brinquedos
    }

    return render(request, 'produtos.html', context)

def alimentacao(request):
    alimentacao = Produto.objects.filter(disponivel=True, categoria='alimentacao').order_by('-id')

    context = {
        'alimentacao': alimentacao
    }
    
    return render(request, 'alimentacao.html', context)

def buscarAlimentacao(request):
    query = request.GET.get('busca')

    if query and busca != '':
        resultado = Produto.objects.filter(nome_produto__icontains=query, disponivel=True, categoria='alimentacao')
    else:
       alimentacao()

    context = {
        'busca': resultado,
    }

    return render(request, 'alimentacao.html', context)

def higiene(request):
    higiene = Produto.objects.filter(disponivel=True, categoria='higiene').order_by('-id')

    context = {
        'higiene': higiene
    }

    return render(request, 'higiene.html', context)

def buscarHigiene(request):
    query = request.GET.get('busca')

    if query and busca != '':
        resultado = Produto.objects.filter(nome_produto__icontains=query, disponivel=True, categoria='higiene')
    else:
        higiene()

    context = {
        'busca': resultado
    }

    return render(request, 'higiene.html', context)

def brinquedos(request):
    brinquedos = Produto.objects.filter(disponivel=True, categoria='brinquedos').order_by('-id')

    context = {
        'brinquedos': brinquedos
    }

    return render(request, 'brinquedos.html', context)

def buscarBrinquedos(request):
    query = request.GET.get('busca')

    if query and busca != '':
        resultado = Produto.objects.filter(nome_produto__icontains=query, disponivel=True, categoria='brinquedos')
    else: 
        brinquedos()
    
    context = {
        'brinquedos': resultado
    }

    return render(request, 'brinquedos.html', context)

def lojas(request):
    petshops = Loja.objects.all().order_by('-id')[:5]
    jdPaulista = Loja.objects.filter(bairro='Jd Paulista').order_by('-id')[:5]
    consolacao = Loja.objects.filter(bairro='Consolação').order_by('-id')[:5]


    context = {
        'lojas': petshops,
        'jdPaulista': jdPaulista,
        'consolacao': consolacao,
    }

    return render(request, 'petshops.html', context)