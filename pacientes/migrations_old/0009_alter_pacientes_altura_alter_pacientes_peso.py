# Generated by Django 4.0.4 on 2022-05-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0008_prontuario_creatinina_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='altura',
            field=models.DecimalField(decimal_places=3, max_digits=3, verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='peso',
            field=models.DecimalField(decimal_places=3, max_digits=3, verbose_name='Peso'),
        ),
    ]
