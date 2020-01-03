from django.db import models
from django.utils import timezone

# Project model
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du projet")
    slug = models.SlugField(max_length=100, null=True)
    image = models.ImageField(upload_to='gallery', null=True, verbose_name="Image du projet")
    labels = models.CharField(max_length=100, null=True, verbose_name="Langages utilisés")
    desc = models.TextField(null=True, verbose_name="Description du projet")
    github = models.CharField(max_length=200, null=True, blank=True, verbose_name="Lien GitHub")
    demo = models.CharField(max_length=200, null=True, blank=True, verbose_name="Lien Démonstration")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de publication")
    
    class Meta:
        verbose_name = "Projet"
        ordering = ['-date']
    
    def __str__(self):
        return self.name

# Upload file in Django Admin
class UploadImg(models.Model):
    projet = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, verbose_name="Nom de l'image")
    link = models.ImageField(upload_to='gallery', null=True, verbose_name="Image")
    
    class Meta:
        verbose_name = "Image"
        ordering = ['-name']

    def __str__(self):
        return self.name