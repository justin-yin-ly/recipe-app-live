# Generated by Django 4.2.14 on 2024-07-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
