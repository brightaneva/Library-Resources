import requests
import json


# due to concurrent us of variable
# is best to the var outside class
# cant call it in the class
headers = {
    "x-rapidapi-host": "covid-193.p.rapidapi.com",
    "x-rapidapi-key": "3574dcf750msh8a2f173c00ee9a0p12b1a8jsn11aee9ef38e3",
}


class Covid_19:
    """Retrieve info on covid around the globe"""

    def all_coun_stats():
        "return info around the globe"

        # api tracks stats in every affected coun
        api_call = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

        # Different headers from 1st headers
        # . api call requires dif headers
        headers = {
            "x-rapidapi-host": "covid-19-coronavirus-statistics.p.rapidapi.com",
            "x-rapidapi-key": "3574dcf750msh8a2f173c00ee9a0p12b1a8jsn11aee9ef38e3",
        }

        return requests.request("GET", api_call, headers=headers).json()

    def stats_on_coun(country_name):
        """retrieve stats on specific coun"""

        # return json on
        # specific country
        api_call = "https://covid-193.p.rapidapi.com/statistics"
        querystring = {"country": country_name}
        return requests.request(
            "GET", api_call, headers=headers, params=querystring
        ).json()

    def coun_afd():
        """return all coun affected"""
        api_call = "https://covid-193.p.rapidapi.com/countries"
        return requests.request("GET", api_call, headers=headers).json()

    def history_coun(coun, date):
        """History of covid in a period"""

        # returns stats on covid
        # in a specific period
        api_call = "https://covid-193.p.rapidapi.com/history"
        querystring = {"country": coun, "day": date}

        return requests.request(
            "GET", api_call, headers=headers, params=querystring
        ).json()

    def store_book(data, bk_name):
        """stores a dic in a json file."""

        with open(f"data/{bk_name}.json", "w") as file:
            json.dump(data, file, indent=4)
            print("Finished Processing")


# history on stats
coun = "canada"

fuc = Covid_19.history_coun(coun,"2021-01-01")
Covid_19.store_book(fuc,f"history_on_{coun}")


fuc = Covid_19.coun_afd()
Covid_19.store_book(fuc,"all_country")
# # print(response.text)

# stat_coun
fuc = Covid_19.stats_on_coun(coun)
Covid_19.store_book(fuc,coun)


fuc = Covid_19.all_coun_stats()
Covid_19.store_book(fuc,"all_stats")
