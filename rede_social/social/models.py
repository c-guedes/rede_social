from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField("Nome", max_length = 128)
    followers = models.ManyToManyField(User,related_name='followers',blank=True)

    def __str__(self):
        return "Usuário: "+self.user.username


class Public(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, verbose_name=("Autor"), on_delete=models.DO_NOTHING,null=True, blank=True)
    pub_text = models.TextField('Conteúdo',max_length = 300)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def get_absolute_url(self):
        return reverse("detalhes", kwargs={"public_id": self.pk})
    
    def __str__(self):
        return "Post feito por:" + " "+self.autor.username

class CommentPub(models.Model):
    autor_comment = models.ForeignKey(User, verbose_name=("Autor"), on_delete=models.DO_NOTHING,null=True, blank=True)
    pub_who = models.ForeignKey(Public, related_name="comentario", on_delete=models.CASCADE, blank=True, null=True)
    coment = models.TextField(verbose_name="Deixe um comentário:")
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentário da Pub'
        verbose_name_plural = 'Comentários da Pub'

   




