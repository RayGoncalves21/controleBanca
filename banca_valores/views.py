from django.shortcuts import render
from banca_valores.models import Banca_valor
from banca_valores.forms import BancaForm
from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404
)

def registrar_banca(request):

    form = BancaForm()


    if request.method == "POST":
        form = BancaForm(request.POST)

        if form.is_valid():
            banca_valor = form.save()
           
            banca_valor.save()

            messages.success(
                request,
                "Banca registrada com sucesso"
            )

            return redirect("index")

    

    context = {
        "nome_pagina": "valor banca",
        "form": form
    }

    return render(request, "registrar_banca.html", context)

def informacoes_banca(request, id):

    banca = get_object_or_404(
        Banca_valor,
        id=id
    )
 
       
    
    context = {
        "nome_pagina": "Informações Banca",
        "banca": banca,
        
    }
    
    return render(request, "informacoes_banca.html", context)