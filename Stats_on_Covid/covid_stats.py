import requests
import json


# due to concurrent us of variable
# is best to the var outside class
# cant call it in the class
headers = {
    "x-rapidapi-host": "covid-193.p.rapidapi.com",
    "x-rapidapi-key": "3574dcf750msh8a2f173c00ee9a0p12b1a8jsn11aee9ef38e3",
}


class Covid_19():
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

    def coun_affected():
        """return all countries affected with covid-19"""
        api_call = "https://covid-193.p.rapidapi.com/countries"
        return requests.request("GET", api_call, headers=headers).json()

    def history_coun(country, date):
        """History of covid in a country in a particular date"""

        # coutry argument take in the name of the country
        #date argument takes in the date in '2021-01-01' format

        api_call = "https://covid-193.p.rapidapi.com/history"
        querystring = {"country": country, "day": date}

        return requests.request(
            "GET", api_call, headers=headers, params=querystring
        ).json()





