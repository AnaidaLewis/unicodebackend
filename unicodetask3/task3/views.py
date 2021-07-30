from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
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
            if (a=="normal") or (a=="fighting") or (a=="flying") or (a=="poison") or (a=="ground") or (a=="rock") or (a=="ghost") or (a=="steel") or (a=="fire") or (a=="water") or (a=="grass") or (a=="elctric") or (a=="psychic") or (a=="ice") or (a=="dragon") or (a=="dark") or (a=="fairy") or (a=="unknown") or (a=="shadow"): 
                b = "https://pokeapi.co/api/v2/type/" + a
                t = requests.get(b).json()
                return render(request,'task3/type_name.html',{'t':t})
            else:
                return render(request,'task3/invalid_error.html')

    else:              
        form = PokemonType()

    response = requests.get("https://pokeapi.co/api/v2/type/").json()
    return render(request,'task3/create.html',{'response':response, 'form':form})
