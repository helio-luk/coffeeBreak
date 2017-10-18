from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import (
    login,
    logout,
    authenticate,
    get_user_model,
    )
from .forms import UserForm, UserLoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):#isso aqui tá bem errado, é pra mudar
    return render(request, 'CoffeeBreak/base.html')

def post_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            novo_usuario = User.objects.create_user(**form.cleaned_data)
            #login(new_user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'CoffeeBreak/new_user.html', {'form': form})

def loginView(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'CoffeeBreak/login.html', {'form': form})
    
def logoutView(request):
    logout(request)
    return redirect('index')