from django.shortcuts import render

# Create your views here.
# Filename: views.py

from django.shortcuts import render
from .models import Pet

# Create your views here.
def home(request):
    # Read all pets from the database
    pets = Pet.objects.all()

    context = {
        'pets': pets
    }
    return render(request, 'home.html', context)