# Generated by Django 4.2.14 on 2024-07-16 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='difficulty',
        ),
    ]