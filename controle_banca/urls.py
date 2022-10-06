
from banca_valores.views import informacoes_banca, registrar_banca
from bilhetes.views import informacoes_bilhete, registrar_bilhete
from dashboard.views import index
from dinheiro.views import mostrar_saldo, registrar_entrada
from django.contrib import admin
from django.urls import include, path
from pagina_inicial.views import pagina_inicial

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        "",
        index,
        name="index",
    ),

    path(
        "registrar-bilhete/",
        registrar_bilhete,
        name="registrar_bilhete",
    ),
    path(
        "bilhetes/<int:id>",
        informacoes_bilhete,
        name="informacoes_bilhete",
    ),
    path(
        "registrar-banca/",
        registrar_banca,
        name="registrar_banca",
    ),
    path(
        "informacoes-banca/",
        informacoes_banca,
        name="informacoes_banca",
    ),
    path(
        "registrar_entrada/",
        registrar_entrada,
        name='registrar_entrada'

    ),
    path(
        "mostrar_saldo/",
        mostrar_saldo,
        name="mostrar_saldo"


    ),
    path("pagina_inicial/", pagina_inicial,
         name="pagina_inicial"),

]
