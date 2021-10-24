import requests
import json

def free_dic(word): 
    """returns synonyms,antonyms,definitions and examples in a json format """   
    
    api_call = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    return requests.request("GET",api_call).json() 