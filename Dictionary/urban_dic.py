from os import name
import requests
import json

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
word = "bright"
querystring = {"term":word}

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "3574dcf750msh8a2f173c00ee9a0p12b1a8jsn11aee9ef38e3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

def store_book(dict, bk_name):
    """stores a dic in a json file."""

    with open(f"data/{bk_name}.json", "w") as file:
        json.dump(dict, file, indent=4)
        print("Finished Processing")


x = response.json()
store_book(x,word)