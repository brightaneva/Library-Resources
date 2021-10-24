import requests
import config
#Live News Data

api_key = config.news_api_key
api_call = f"http://api.mediastack.com/v1/news?access_key={api_key}"


class News():
    def current_news(self,countries="us",categories="health,entertainment"):
        "returns business and sports news of us and au by defult"
        quarystring = {"languages":"en","country":countries,"limit":"100","categories":categories}

        return requests.request("GET",api_call,params=quarystring).json()




# optional parameters: 

#     & sources = cnn,bbc
#     & categories = business,sports
#     & countries = us,au
#     & languages = en,-de
#     & keywords = virus,-corona
#     & sort = published_desc
#     & offset = 0
#     & limit = 100