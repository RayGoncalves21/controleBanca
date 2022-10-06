from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from dinheiro.forms import DinheiroForm
from dinheiro.models import Dinheiro


def mostrar_saldo(request):
    bancas = Dinheiro.objects.all()
    return render(request, 'mostrar_saldo.html', {'bancas': bancas})


def registrar_entrada(request):
    form = DinheiroForm()

    if request.method == "POST":
        form = DinheiroForm(request.POST)

        if form.is_valid():
            dinheiro = form.save()
            dinheiro.save()

        messages.success(
            request,
            'Banca Registrada com sucesso'
        )

        return redirect('index')

    context = {
        "nome_pagina": "registrar_banca",
        "form": form
    }

    return render(request, 'registrar_entrada.html', context)
