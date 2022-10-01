from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField


class Books(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    estado = models.CharField(max_length=15)
    autor = models.CharField(max_length=200)
    reseña = RichTextField(blank=True, null=True)
    libro_img = models.ImageField(null=True, blank=True, upload_to="images/")
    fecha = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='book_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.titulo+'|'+str(self.usuario)

    def get_absolute_url(self):
        return reverse('book_details', args=[str(self.pk)])


class Categorias(models.Model):
    categoria = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.categoria

    def get_absolute_url(self):
        return reverse('index')