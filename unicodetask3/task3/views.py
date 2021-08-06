from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
import requests
import json 
from .forms import PokemonType, PokemonDetails
from .models import Pokemon

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
            url = requests.get("https://pokeapi.co/api/v2/type/").json()
            result = url['results']
            pTypeName = []
            for i in result:
                name = i['name']
                pTypeName.append(name)
            if a not in pTypeName:
                return render(request,'task3/invalid_error.html')
            else:
                b = "https://pokeapi.co/api/v2/type/" + a
                t = requests.get(b).json()
                return render(request,'task3/type_name.html',{'t':t, 'pTypeName':pTypeName})
                
    else:              
        form = PokemonType()

    response = requests.get("https://pokeapi.co/api/v2/type/").json()
    return render(request,'task3/create.html',{'response':response, 'form':form})


def details (request):
    if request.method == "POST":
        form = PokemonDetails(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            a = n.lower()
            url = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1118").json()
            result = url['results']
            pName = []
            for i in result:
                name = i['name']
                pName.append(name)
            if a not in pName:
                return render(request,'task3/invalid_pokemon.html')
            else:  
                db = Pokemon(name = a )
                db.save()
                pokemon = "https://pokeapi.co/api/v2/pokemon/" + a
                t = requests.get(pokemon).json()
                id = str(t['id'])
                pic = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + id + ".png"
                return render(request,'task3/name_details.html',{'t':t, 'n':n, 'pic':pic })
        

    else:              
        form = PokemonDetails()  

    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1118").json()
    return render(request,'task3/details.html',{'response':response, 'form':form})

    
            