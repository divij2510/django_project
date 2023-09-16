# pokedex/views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests

def get_pokemonimage(type):
  
    api_url = f'https://pokeapi.co/api/v2/pokemon/{type}/'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
      
        image_url = data['sprites']['front_default'] if 'sprites' in data else ''
        return image_url
    else:
        return ''

def pokemon_names(request):
   
    api_url = 'https://pokeapi.co/api/v2/type/'
    response = requests.get(api_url)

    api_url2 = 'https://pokeapi.co/api/v2/pokemon/'
    response2 = requests.get(api_url2)
    pokemons_data=response2.json()
    pokemons=pokemons_data['results']

    if response.status_code == 200:
        data = response.json()
        types = data['results']
        
       
        html_response = "<h1>Pokemon Types</h1>"
        html_response += "<ul>"
        for entry,entry2 in zip(types,pokemons):
            type_name = entry['name']
            pokeId=entry2['url'].replace("https://pokeapi.co/api/v2/pokemon/",'')
            image_url = get_pokemonimage(pokeId)
            html_response += f"<li><img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/2.png' alt='{type_name}' width='30' height='30'> {type_name}</li>"
        html_response += "</ul>"
        return HttpResponse(html_response)
    else:
        return HttpResponse('Failed to fetch data from PokeAPI')


