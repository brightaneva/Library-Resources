from basic_search import BS,Filter_BS
from render_search import RS,Filter_RS
from helpers import store_book
from quote_generator import Quote_Generator 
import time

name = "coke"
x = RS().book_title(name)
store_book(x,name)

# x = ad.book_title("superman") 

# start_time = time.time()
# store_book(x,"random_quote")

# print("--- %s seconds ---" % (time.time() - start_time))


