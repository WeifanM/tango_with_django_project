from django.shortcuts import render
# Import the Category model
from rango.models import Category
from django.http import HttpResponse

#def index(request):
  #  return HttpResponse("Rango says hey there partner!")

def index(request):
# Construct a dictionary to pass to the template engine as its context.
# Note the key boldmessage matches to {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #return render(request, 'rango/index.html', context=context_dict)
###Feb-1-2024
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!) # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
        # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)