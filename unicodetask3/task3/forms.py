from django import forms

class PokemonType(forms.Form):
    name = forms.CharField(label = "Enter pokemon type", max_length =200)
    check = forms.BooleanField()

        
