from io import BytesIO 
import base64
import matplotlib.pyplot as plt
from .models import Recipe

def get_recipe_difficulty_from_id(val):
    recipe_difficulty = Recipe.objects.get(id=val).calculate_difficulty()
    return recipe_difficulty

def get_graph():
   #create a BytesIO buffer for the image
   buffer = BytesIO()         

   #create a plot with a bytesIO object as a file-like object. Set format to png
   plt.savefig(buffer, format='png')

   #set cursor to the beginning of the stream
   buffer.seek(0)

   #retrieve the content of the file
   image_png=buffer.getvalue()

   #encode the bytes-like object
   graph=base64.b64encode(image_png)

   #decode to get the string as output
   graph=graph.decode('utf-8')

   #free up the memory of buffer
   buffer.close()

   #return the image/graph
   return graph

#chart_type: user input o type of chart,
#data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
   #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
   #AGG is preferred solution to write PNG files
   plt.switch_backend('AGG')

   #specify figure size
   fig=plt.figure(figsize=(6,3))

   #select chart_type based on user input from the form
   if chart_type == '#1':
        #plot bar chart between date on x-axis and quantity on y-axis
        plt.bar(data['name'], data['cooking_time'])
        plt.ylabel('Cooking Time')

   elif chart_type == '#2':
       #generate pie chart based on difficulty occurence

       occurences = {}
       for i in data['difficulty']:
        if i == "Easy":
            if not "Easy" in occurences:
                occurences["Easy"] = 0
            occurences["Easy"] += 1
        elif i == "Medium":
            if not "Medium" in occurences:
                occurences["Medium"] = 0
            occurences["Medium"] += 1
        elif i == "Intermediate":
            if not "Intermediate" in occurences:
                occurences["Intermediate"] = 0
            occurences["Intermediate"] += 1
        elif i == "Hard":
            if not "Hard" in occurences:
                occurences["Hard"] = 0
            occurences["Hard"] += 1
                    
       plt.pie(occurences.values(), labels=occurences.keys())
       plt.title('Distribution of Recipe Difficulties')

   else:
       print ('unknown chart type')

   #specify layout details
   plt.tight_layout()

   #render the graph to file
   chart =get_graph() 
   return chart       