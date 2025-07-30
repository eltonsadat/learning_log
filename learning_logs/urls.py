"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #name vem depois
    path('topics', views.topics, name='topics'), #cria após as mudanças do index.html
    path('topics/<topic_id>/', views.topic, name='topic'), #cria após finalizar topics.html
    path('new_topic', views.new_topic, name='new_topic'), #cria na aula de formularios
    path('success', views.success, name='success'), #exercício
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'), #cria na aula de anotações
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'), #Cria na aula de editar_anotações
    path('delete_entry/<entry_id>', views.delete_entry, name='delete_entry'), #Exercício 2

]
