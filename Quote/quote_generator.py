from quote import quote
import requests
from requests.exceptions import RequestsWarning

class Quote_Generator():
    """Generate some quotes of famous
    people and anime quote"""


    def random_quote(self):
        "fetches random quote from quotable api"
        return requests.get("https://api.quotable.io/random").json()

    def quote_by(self,name):
        """return quotes said in books

        Args:
            name ([name]): [name of the person quote]

        Returns:
            [json]: [data of the author,book and quote]
        """
        self.name = name
        return quote(self.name)

    def random_anime_quote(self):
        return requests.get("https://animechan.vercel.app/api/random").json()
    
    def top_anime_quote(self):
        return requests.get("https://animechan.vercel.app/api/quotes").json()
    
    def anime_quote_title(self,title):
        """quote in an anime 

        Args:
            title ([title]): [title of the anime]

        Returns:
            [json]: [data of the anime and the quote in it]
        """

        self.title = title
        url = f"https://animechan.vercel.app/api/quotes/anime?title={self.title}"
        return requests.get(url).json()

    def anime_quote_by(self,name):
        """quote of an anime character

        Args:
            name ([name]): [name of the anime character you want quote from]

        Returns:
            [json]: [name of the anime character and quote and the anime he said it]
        """
        self.name = name
        url = f"https://animechan.vercel.app/api/quotes/character?name={self.name}&?page=5"
        return requests.get(url).json()