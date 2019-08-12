from django.urls import path
from social import views as core_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

urlpatterns = [
    path('index', core_views.getHome,name='index'),
    path('novapub', core_views.postPub, name='novapub'),
    path('perfil/<str:user>', core_views.get_profile, name='perfil'),
    url('', auth_views.LoginView.as_view(), name = 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('pub/<int:public_id>/', core_views.pubs_detail, name = 'detalhes'),
    path('<str:user>/', core_views.profile_follow, name = 'seguir'),
    #path('noticias/resumo/', noticias_resumo,name='request'),
    #path('resumo/', noticias_resumo_template,name='request'),
    #path('detalhe/<int:noticia_id>', noticia_detalhes,name='detalhes'),
    #path('detalhe/noticia_tags/<str:tag>', noticias_with_tag,name='noticeWithTag'),
    #path('contato/', ContatoView.as_view(),name='contato'),
    #path('contato/sucesso', ContatoSucessoView.as_view(),name='contato_sucesso'),
]
