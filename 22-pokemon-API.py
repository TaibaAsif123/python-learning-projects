
"""
This program connects to the PokeAPI to fetch and display information about a
specific Pokémon (name, ID, height, weight) using HTTP requests and JSON parsing
"""
#How to Connect to API
#response is object that returns status code
#Informational responses (100 – 199)
#Successful responses (200 – 299)
#Redirection messages (300 – 399)
#Client error responses (400 – 499)
#Server error responses (500 – 599)
import requests

base_url="https://pokeapi.co/api/v2/"
def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code==200:
       pokemon_data=response.json() #convert json file to python
       #difficult to read
       #print(pokemon_data)
       return pokemon_data
    else:
        print(f"failed to retrieve data {response.status_code}")



pokemon_name="pikachu"
#dictionary retrieved
pokemon_info=get_pokemon_info(pokemon_name)
if pokemon_info:
    print(f"Name:{pokemon_info['name'].capitalize()}")
    print(f"ID:{pokemon_info['id']}")
    print(f"Height:{pokemon_info['height']}")
    print(f"Weight:{pokemon_info['weight']}")
 