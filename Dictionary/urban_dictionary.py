import requests
import json


#The urban dictionry is a dictionary of profane meanings
#Not a real dictionary
def urban_dic(word):
    """return pronounciations and meanings in profane language"""
    api_call = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    
    querystring = {"term":word}

    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "3574dcf750msh8a2f173c00ee9a0p12b1a8jsn11aee9ef38e3"
        }

    #returns the profane meaning of a word
    return requests.request("GET", api_call, headers=headers, params=querystring).json()




