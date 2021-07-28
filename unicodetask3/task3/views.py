from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .forms import PokemonType

# Create your views here.
def home(request):
    response = requests.get("https://pokeapi.co/api/v2/type/").json()
    return render(request,'task3/home.html',{'response':response})

def create(request):
    if request.method == "POST":
        form = PokemonType(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            a = n.lower()
            b = "https://pokeapi.co/api/v2/type/" + a
            t = requests.get(b).json()
            return render(request,'task3/type_name.html',{'t':t})


    else:
        form = PokemonType()

    response = requests.get("https://pokeapi.co/api/v2/type/").json()
    return render(request,'task3/create.html',{'response':response, 'form':form})
