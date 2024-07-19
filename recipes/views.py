from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from .utils import get_recipe_difficulty_from_id, get_chart

#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# import search form
from .forms import RecipesSearchForm

import pandas as pd

# Create your views here.
def home(request):
    return render(request,'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name='recipes/main.html'
    object_list = []

    # Load recipes on initial list rendering
    def get(self, request):
        context = self.get_context_data()
        context["recipes"] = Recipe.objects.all()

        return render(self.request, "recipes/main.html",context)

    # When the search button is pressed, it makes a POST request. This is where we filter and return our data.
    def post(self, request):

        recipes = None
        recipes_df = None
        chart = None

        user_input = request.POST.get('text_input')
        filter_type = request.POST.get('filter_type')
        chart_type = request.POST.get('chart_type')

        if user_input == "":
            qs = Recipe.objects.all()
        else:
            if filter_type == '#1':
                qs = Recipe.objects.filter(name__icontains=user_input)
            elif filter_type == '#2':
                qs = Recipe.objects.filter(ingredients__icontains=user_input)
        
        context = self.get_context_data()
        if qs:
            recipes = qs
            recipes_df=pd.DataFrame(qs.values())
            recipes_df['difficulty']=recipes_df['id'].apply(get_recipe_difficulty_from_id)
            
            # Testing manual datafram input
            # recipes_df['all']=['a','b','c','d','e']
            
            chart = get_chart(chart_type, recipes_df)
        
        context["recipes"] = recipes
        context["recipes_df"] = recipes_df
        context["chart"] = chart

        return render(self.request, "recipes/main.html", context)
    
    # Lets us render the form onto the main list view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RecipesSearchForm()
        context["form"] = form
        return context

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name='recipes/detail.html'