from django.shortcuts import render

# Create your views here.
#Uma view é o lugar onde nós colocamos a "lógica" da nossa aplicação. Ela vai extrair informações do model que você criou e entregá-las a um template.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
