# Generated by Django 4.2.14 on 2024-07-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ingredients', models.CharField(max_length=255)),
                ('cooking_time', models.IntegerField()),
                ('difficulty', models.CharField(choices=[('hard', 'Hard'), ('medium', 'Medium'), ('interediate', 'Intermediate'), ('unknown', 'Unknown'), ('easy', 'Easy')], default='unknown', max_length=20)),
            ],
        ),
    ]