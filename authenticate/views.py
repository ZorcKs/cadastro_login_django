from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome_usuario = request.POST.get('nome_usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        usuario = User.objects.filter(username=nome_usuario).first()
    
        if usuario:
            return render(request, 'cadastro.html',{'usuario':usuario})
    
        usuario = User.objects.create_user(username=nome_usuario,email=email,password=senha)
        usuario.save()
        return redirect('url_login')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        nome_usuario = request.POST.get('nome_usuario')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome_usuario,password=senha)
    
        if usuario:
            login_django(request, usuario)
            return redirect('url_inicial')
        else:
            senha = User.objects.filter(password=senha).exists()
            return render(request,'login.html', {'senha':senha})
        
@login_required(login_url='login/')
def inicial(request):
    return render(request, 'pg_inicial.html')
