from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Sessao(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField("Tipo", max_length=100)
    horario = models.DateTimeField()
    perido = models.CharField("Perído", max_length=100, null=True, blank=True)
    desconforto_fisico = models.IntegerField(
        verbose_name="Desconforto Fisico",
        null=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    desconforto_mental = models.IntegerField(
        verbose_name="Desconforto Metal",
        null=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    superado = models.BooleanField("Superado", default=False)
    notas = models.TextField(verbose_name="Notas", null=True, blank=True)

    def __str__(self):
        return str(self.horario)


TIPOS_CHOICES = [
    ("paciente", "PACIENTE"),
    ("terapeuta", "TERAPEUTA"),
]


class Contatos(models.Model):
    telefone = models.CharField("Telefone", max_length=20, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)

    def __str__(self):
        ref = self.email if self.email else self.telefone
        return ref


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sessao = models.ManyToManyField("Sessao", null=True, blank=True)
    pacientes = models.ManyToManyField("Profile", null=True, blank=True)
    contatos = models.ForeignKey("Contatos", on_delete=models.CASCADE, null=True)

    tipo = models.CharField("Tipo", max_length=100, choices=TIPOS_CHOICES)
    foto = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return self.user.username
