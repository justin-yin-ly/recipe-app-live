from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=50)
    pic=models.ImageField(upload_to='recipes',default='no_picture.jpg')
    ingredients=models.CharField(max_length=255)
    cooking_time=models.IntegerField()
    # Not being used, but I'm leaving it here for if I can figure out how to make it work with the form
    difficulty=models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    def calculate_difficulty(self):
        ingredients_list = self.ingredients.split(', ')
        if self.cooking_time < 10:
            if len(ingredients_list) < 4:
                return "Easy"
            else:
                return "Medium"
        else:
            if len(ingredients_list) < 4:
                return "Intermediate"
            else:
                return "Hard"
            
    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk':self.pk})