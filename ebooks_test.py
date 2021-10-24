from Ebooks.basic_search import Basic_Search as bs, Advance_Search as ad
from helpers import store_data

#to get json of ebook
normal_search = bs().book_title("coke")

#To search for ebook by an author
author_search = bs().author_name("coke")

#Todo get a particular set of data use the filters
#define filter in a dictionary and pass it to the
#filter_title fuction
dic = {"Year":"2010","Language":"English","Extension":"pdf"}
filter_search = bs().filter_title("coke",dic,False)

#Advanced_search filters by author
dic = {"Year":"2010","Language":"English","Extension":"pdf"}
filter_author = bs().filter_author("coke",dic,False)


#Todo get both download links and cover of the ebook 

#In your json result, call the Advance_search class
advanced_search = ad().book_title("coke")

#To search for ebook by an author
author_ad_search = ad().author_name("coke")

#Advanced_search filters 
dic = {"Year":"2010","Language":"English","Extension":"pdf"}
filter_ad_search = ad().filter_title("coke",dic,False)

#Advanced_search filters by author
dic = {"Year":"2010","Language":"English","Extension":"pdf"}
filter_ad_author = ad().filter_author("coke",dic,False)


#call the store_data module and store the data
#TODO Basic_Search() 
store_data(normal_search,"normal_search")
store_data(author_search,"author_search")
store_data(filter_search,"filter_search")
store_data(filter_author,"filter_author")

#TODO Advance_Search()
store_data(advanced_search,"advanced_search")
store_data(author_ad_search,"author_ad_search")
store_data(filter_ad_search,"filter_ad_search")
store_data(filter_ad_author,"filter_ad_author")

