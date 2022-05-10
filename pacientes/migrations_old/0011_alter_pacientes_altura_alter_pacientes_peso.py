# Generated by Django 4.0.4 on 2022-05-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0010_rename_endereço_pacientes_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='altura',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Peso'),
        ),
    ]
