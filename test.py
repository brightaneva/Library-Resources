from Ebooks.basic_search import Basic_Search
from Ebooks.render_search import RS
from Ebooks.helpers import store_book
from Quote.quote_generator import  Quote_Generator
import time

start_time = time.time()
name = "boy"
x = Basic_Search().book_title(name)
store_book(x,name)

print("--- %s seconds ---" % (time.time() - start_time))
# x = ad.book_title("superman") 


# store_book(x,"random_quote")



