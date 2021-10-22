# from _typeshed import Self

import requests
import json


headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "3574dcf750msh8a2f173c00ee9a0p12b1a8jsn11aee9ef38e3"
            }
coun_url = "https://covid-193.p.rapidapi.com/statistics"
all_coun = "https://covid-193.p.rapidapi.com/countries"


class Covid_19():        
    
    def stats_on_coun(self,country_name):
        self.country_name = country_name
        querystring = {"country":self.country_name}
        return requests.request(
            "GET", coun_url, headers=headers, params=querystring
        ).json()

    def coun_afd():
        return requests.request(
            "GET", all_coun, headers=headers
        ).json()
        
    
    
    def store_book(dict, bk_name):
        """stores a dic in a json file."""

        with open(f"data/{bk_name}.json", "w") as file:
            json.dump(dict, file, indent=4)
            print("Finished Processing")



# name = "ghana"
fuc = Covid_19.coun_afd()
Covid_19.store_book(fuc,"all_country")
# print(response.text)