from .crawler import quote
import requests


class Quote_Generator():
    """Generate some quotes of famous
    people and anime quote"""


    def random_quote():
        "fetches random quote from quotable api"
        return requests.get("https://api.quotable.io/random").json()

    def quote_by(name):
        """return quotes said in books

        Args:
            name ([name]): [name of the person quote]

        Returns:
            [json]: [data of the author,book and quote]
        """
        return quote(name)

    def random_anime_quote():
        return requests.get("https://animechan.vercel.app/api/random").json()
    
    def top_anime_quote():
        return requests.get("https://animechan.vercel.app/api/quotes").json()
    
    def anime_quote_title(title):
        """quote in an anime 

        Args:
            title ([title]): [title of the anime]

        Returns:
            [json]: [data of the anime and the quote in it]
        """
        url = f"https://animechan.vercel.app/api/quotes/anime?title={title}"
        return requests.get(url).json()

    def anime_quote_by(name):
        """quote of an anime character

        Args:
            name ([name]): [name of the anime character you want quote from]

        Returns:
            [json]: [name of the anime character and quote and the anime he said it]
        """
        url = f"https://animechan.vercel.app/api/quotes/character?name={name}&?page=5"
        return requests.get(url).json()