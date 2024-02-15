from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    
    #verificar se o usuário está logado:
    if request.method == 'POST':
        email = request.POST['input_email']
        password = request.POST['input_password']
        user = authenticate(request, username=email, password=password) 
        if user is not None:
            login(request, user)
            messages.sucess(request, "Logado com Sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Erro no login, tente novamente")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    

def register_user(request):
    return render(request, 'register.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout_user(request)
    messages.success(request, "Você foi deslogado")
    return redirect('home')