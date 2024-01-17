from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('novo_flashcard'))
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            
            return redirect(reverse('cadastro'))
            
        
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome')
            
            
            return redirect(reverse('cadastro'))
        
        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
            return redirect(reverse('login'))
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect(reverse('cadastro'))
            

def login(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
             return redirect(reverse('novo_flashcard'))
        return render(request,'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Bem vindo')
            return redirect(reverse('novo_flashcard'))
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect(reverse('login'))
  
def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))