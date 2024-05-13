# Create your views here.

from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import Usuario
import hashlib

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/cursos/home/')
    
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def login(request):
    
    if request.session.get('usuario'):
        return redirect('/cursos/home/')
    
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    usuario = Usuario.objects.filter(email = email)
    
    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=2')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome,
                          email=email,
                          senha=senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')
    
    
def valida_login(request):
    # if request.session.get('usuario'):
    #     return redirect('/cursos/home/')
    
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = hashlib.sha256(senha.encode()).hexdigest()
    usuario = Usuario.objects.filter(email = email).filter(senha = senha)
    #print(usuario)
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/cursos/home/')
    
    
def sair(request):
    request.session.flush()
    return redirect('/auth/login/')