from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate #login, authenticate - aula register
#register
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Faz logout do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Faz cadastro de um novo usuário"""
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)