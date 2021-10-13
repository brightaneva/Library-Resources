from Ebooks.basic_search import BS,Filter_BS
from Ebooks.render_search import RS,Filter_RS
from Ebooks.helpers import store_book
from Quote.quote_generator import  Quote_Generator
import time

name = "boy"
x = RS().book_title(name)
store_book(x,name)

# x = ad.book_title("superman") 

# start_time = time.time()
# store_book(x,"random_quote")

# print("--- %s seconds ---" % (time.time() - start_time))


