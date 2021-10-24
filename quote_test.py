from Quote.quote_generator import Quote_Generator as qt
from helpers import store_data


#search for quote by a famous celebraty
person_quote = qt.quote_by("elon_musk")

#return random quote
random_quotes = qt.random_quote()

#search for quote by an anime character
anime_charac_quote = qt.anime_quote_by("Madara")

#random anime quote
random_anime_quotes = qt.random_anime_quote()

#all quotes said in a particular anime
quotes_in_anime = qt.anime_quote_title("Naruto Shippuden")

#return top anime quote 
top_quote = qt.top_anime_quote()


store_data(person_quote,"person_quote")
store_data(random_quotes,"random_quotes")
store_data(anime_charac_quote,"anime_charac_quote")
store_data(random_anime_quotes,"random_anime_quotes")
store_data(quotes_in_anime,"quotes_in_anime")
store_data(top_quote,"top_quote")