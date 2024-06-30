import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contatos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sessao",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("tipo", models.CharField(max_length=100, verbose_name="Tipo")),
                ("horario", models.DateTimeField()),
                (
                    "perido",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Perído"
                    ),
                ),
                (
                    "desconforto_fisico",
                    models.IntegerField(
                        default=0,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                        verbose_name="Desconforto Fisico",
                    ),
                ),
                (
                    "desconforto_mental",
                    models.IntegerField(
                        default=0,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                        verbose_name="Desconforto Metal",
                    ),
                ),
                (
                    "superado",
                    models.BooleanField(default=False, verbose_name="Superado"),
                ),
                (
                    "notas",
                    models.TextField(blank=True, null=True, verbose_name="Notas"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[("paciente", "PACIENTE"), ("terapeuta", "TERAPEUTA")],
                        max_length=50,
                        verbose_name="Tipo",
                    ),
                ),
                (
                    "foto",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics"),
                ),
                (
                    "contatos",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.contatos",
                    ),
                ),
                (
                    "pacientes",
                    models.ManyToManyField(blank=True, null=True, to="core.profile"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sessao",
                    models.ManyToManyField(blank=True, null=True, to="core.sessao"),
                ),
            ],
        ),
    ]