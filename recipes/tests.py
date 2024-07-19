from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm
from django.contrib.auth.models import User

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        # Set up an object to test with
        Recipe.objects.create(name='Tea',ingredients='Tea Leaves, Sugar, Water',cooking_time=5)
    
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        
        self.assertEqual(field_label,'name')

    def test_recipe_name_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length

        self.assertEqual(max_length, 50)
    
    def test_ingredients_length(self):
        recipe = Recipe.objects.get(id=1)       
        max_length = recipe._meta.get_field('ingredients').max_length

        self.assertEqual(max_length, 255)
    
    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        cooking_time = recipe.cooking_time

        self.assertTrue(cooking_time > -1)

    def test_difficulty(self):
        recipe = Recipe.objects.get(id=1)
        difficulty = recipe.calculate_difficulty()

        self.assertEqual(difficulty, "Easy")
    
    def test_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

class RecipeSearchTest(TestCase):
    def setUpTestData():
        # Set up an object to test with
        Recipe.objects.create(name='Tea',ingredients='Tea Leaves, Sugar, Water',cooking_time=5)

    def setUp(self):
        # Make a fake user to run authentication tests with
        self.user = User.objects.create_user(username="recipebot",password="trustmeimachef")
        self.client.login(username="recipebot",password="trustmeimachef")

    # Test that input is valid
    def test_form_valid(self):
        form_data = {
            'text_input': 'Tea',
            'filter_type': '#1',
            'chart_type': '#1'
        }

        form = RecipesSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Test that we get redirected if we're logged out and try to look at the recipes
    def test_authentication(self):
        self.client.logout()
        response = self.client.get("/list/")
        self.assertRedirects(response, "/login/?next=/list/")