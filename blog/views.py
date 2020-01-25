from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post#importamos o modelo para a view

# Create your views here.
#Uma view é o lugar onde nós colocamos a "lógica" da nossa aplicação. Ela vai extrair informações do model que você criou e entregá-las a um template.
def post_list(request):#posts é o nome do nosso QuerySet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})