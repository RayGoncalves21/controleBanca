from django.urls import path

from pagina_inicial.views import pagina_inicial

urlpatterns = [
    path('pagina_inicial/', pagina_inicial),  # Home


]
