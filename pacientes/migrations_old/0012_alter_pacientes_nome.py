# Generated by Django 4.0.4 on 2022-05-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0011_alter_pacientes_altura_alter_pacientes_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
    ]
