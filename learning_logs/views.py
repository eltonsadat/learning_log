from django.shortcuts import render
from .models import Topic, Entry #Entry importa na aula de editar_anotações
#imports aula formularios
from .forms import TopicForm, EntryForm #EntryForm - aula de anotações
from django.http import HttpResponseRedirect, Http404 #aula vinculo
from django.urls import reverse
#restrinções
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """Página principal do Learning Log"""
    return render (request, 'learning_logs/index.html')

#depois de editar o index.html ^ import
@login_required
def topics(request):
    """Mostra todos os assuntos"""
    #aula vinculo
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render (request, 'learning_logs/topics.html', context)

#após crirar a url do topic
@login_required
def topic(request, topic_id):
    """Mostra o assunto e todas as suas entradas"""
    topic = Topic.objects.get(id = topic_id)

    #Aula vinculo
    ##Garante que a anotação pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

#Aula de formulários ^ import ------------------------------------------------
@login_required
def new_topic(request):
    """Adiciona um novo assunto"""
    if request.method != 'POST':
        #nenhum dado submetido, cria formulario em branco
        form = TopicForm()
    else:
        #dados de POST submentidos, processa dados
        form = TopicForm(request.POST)
        if form.is_valid():
            
            #Aula vinculo
            ##vincular o novo tópico ao criador   
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('success')) #'topics'
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

#Exercício
@login_required
def success(request):
    """Formulário enviado com sucesso"""
    topic = Topic.objects.last()
    context = {'topic': topic}
    return render (request, 'learning_logs/success.html', context)

#Aula de anotações ^import EntryForm ---------------------------------------
@login_required
def new_entry(request, topic_id):
    """Acrescenta um assunto para o tópico"""
    topic = Topic.objects.get(id=topic_id)

    #Aula vinculo
    ##Garante que a anotação pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #nenhum dado submetido, cria formulario em branco
        form = EntryForm()
    else:
        #dados de POST submentidos, processa dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
        
    context = {'topic':topic, 'form':form}    
    return render(request, 'learning_logs/new_entry.html', context)

#Aula de editar_anotações ^import Entry
@login_required
def edit_entry(request, entry_id):
    """Edita um tópico existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    #Aula vinculo
    ##Garante que a anotação pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Requisiçaõ inicial. Preenche proviamente o formulário com a entrada atual
        form = EntryForm(instance=entry)
    else:
        #Dados POST submentidos. Processa dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

#EXERCÍCIO 2
@login_required
def delete_entry(request, entry_id):
    """Apaga a entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic_id = entry.topic.id  # guarda o topic.id antes de apagar
    entry.delete()
    return HttpResponseRedirect(reverse('topic', args=[topic_id]))