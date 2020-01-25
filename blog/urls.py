from django.urls import path # importando a função do django url 
from . import views# importando todas as nossas views do aplicativo blog

urlpatterns = [#abaixo atribuímos uma view chamada post_list à URL raiz
    path('', views.post_list, name='post_list'),#post_list é nome da url que será usada para identificar a view
]
