from django import forms    #import django forms

CHART__CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   )

FILTER__CHOICES = (
    ('#1', 'Name'),
    ('#2', 'Ingredient'),
)

#define class-based Form imported from Django forms
class RecipesSearchForm(forms.Form): 
    text_input= forms.CharField(max_length=120, required=False)
    filter_type = forms.ChoiceField(choices=FILTER__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)