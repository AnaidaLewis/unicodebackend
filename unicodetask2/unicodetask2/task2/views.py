from django.shortcuts import render
from django.http import HttpResponse
import requests 
import json

# Create your views here.

def home(response):
    return HttpResponse(" <h1>Home Page</h1> ")

def types(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100').json()
    return render(request, 'task2/home.html',{'response':response})