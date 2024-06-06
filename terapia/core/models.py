from django.db import models

class Terapeuta(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Terapeutas'
        ordering = ('nome', )




