# Generated by Django 4.2.4 on 2024-01-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portafolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={
                "ordering": ["-created"],
                "verbose_name": "proyecto",
                "verbose_name_plural": "proyectos",
            },
        ),
        migrations.AlterField(
            model_name="project",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Fecha de creación"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(verbose_name="Descripción"),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="", verbose_name="Imagen"),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Título"),
        ),
        migrations.AlterField(
            model_name="project",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición"),
        ),
    ]