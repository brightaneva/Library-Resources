from helpers import store_data
from News.news import News

#give you current news in the us
current_new = News().current_news()
# optional parameters: 

#     & sources = cnn,bbc
#     & categories = business,sports
#     & countries = us,au
#     & languages = en,-de
#     & keywords = virus,-corona
#     & sort = published_desc
#     & offset = 0
#     & limit = 100



store_data(current_new,"current_news")
