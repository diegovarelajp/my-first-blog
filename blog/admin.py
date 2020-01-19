#Para adicionar, editar e deletar os posts que modelamos, nós usaremos o admin do Django.
from django.contrib import admin
from .models import Post #estamos importando a class Post que criamos no models.py

admin.site.register(Post)#Para tornar nosso modelo visível na página de administração, precisamos registrá-lo

