from django.http import *
from django.urls import reverse
from django.views.generic import ListView, FormView,TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as teste, logout as brabor, authenticate
from django.core.paginator import Paginator
from .models import *
from .forms import *

def postPub(request):
    if request.method == 'POST':
        form = PublicForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.refresh_from_db() 
            form.autor = request.user
            form.save()
            #form.titulo = form.cleaned_data.get('titulo')
            #form.conteudo = form.cleaned_data.get('conteudo')
            #form.foto = form.cleaned_data.get('foto')
            #form.save()
            #return HttpResponse(resp)
            return HttpResponseRedirect('index')
    else:
        form = PublicForm()

    return render(request, 'social/publicar.html', {'form': form})


def getHome(request):
    pubs = Public.objects.all().order_by('data').reverse()
    users = User.objects.all()

    print(pubs)
    
    return render(request, 'social/index.html',{'pubs':pubs, 'usuarios':users})

def get_profile(request,user):
    try:
        profile = User.objects.get(username=user)
        pubs = Public.objects.all().filter(autor = profile)
        print(pubs)
    except Public.DoesNotExist:
        raise Http404('User não encontrado')

    return render(request, 'social/perfil.html', {'pubs':pubs})

def profile_follow(request,user):
    follow = User.objects.get(username=user)
    post = get_object_or_404(Profile, follow)
    if post.tops.filter(id=request.user.id).exists():
        post.followers.remove(request.user)
        #is_top = False
    else:
        post.followers.add(request.user)
        #is_top = True
    return HttpResponseRedirect("/")

    

def pubs_detail(request,public_id):
    try:
        pub = Public.objects.get(pk = public_id)
        comentarios = CommentPub.objects.all()
        coments = comentarios.filter(pub_who=pub)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                print("val")
                form = form.save()
                form.refresh_from_db()
                form.pub_who = pub
                form.autor_comment = request.user
                form.save()
                #form.titulo = form.cleaned_data.get('titulo')
                #form.conteudo = form.cleaned_data.get('conteudo')
                #form.foto = form.cleaned_data.get('foto')
                #form.save()
                #return HttpResponse(resp)
                return HttpResponseRedirect("/")
        else:
            form = CommentForm()

    except Public.DoesNotExist:
        raise Http404('Publicação não encontrada')

    return render(request, 'social/detalhes.html', {'pub':pub,'coments':coments,'form':form,})