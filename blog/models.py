from django.conf import settings
from django.db import models
from django.utils import timezone
#CLASS é uma palavra-chave especial que indica que estamos definindo um objeto.
#POST é o nome do nosso modelo
#models.Model significa que o Post é um modelo de Django, então o Django sabe que ele deve ser salvo no banco de dados.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# este é um link para outro modelo.
    title = models.CharField(max_length=200)#é assim que definimos um texto com um número limitado de caracteres.
    text = models.TextField()# este campo é para textos sem um limite fixo.
    created_date = models.DateTimeField(default=timezone.now)#este é uma data e hora.
    published_date = models.DateTimeField(blank=True, null=True)
    #As duas funções/métodos estão endentadas dentro da Class Post, pois pertence a ela.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#O método str retornará um texto(string) com o título do Post
        return self.title