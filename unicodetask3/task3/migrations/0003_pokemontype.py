# Generated by Django 3.2.5 on 2021-08-06 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task3', '0002_rename_apirequests_pokemon'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
