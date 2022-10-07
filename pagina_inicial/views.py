from bilhetes.forms import AtualizaBilheteForm, BilheteForm
from bilhetes.models import Bilhete
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.utils import timezone


def pagina_inicial(request):

    todos_bilhetes = Bilhete.objects.all()

    context = {
        "nome_pagina": "Inicio da dashboard",
        'todos_bilhetes': todos_bilhetes,

    }
    return render(request, "pagina_inicial.html", context)
