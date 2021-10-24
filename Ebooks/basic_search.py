import json
import time
from .search_request import *
from .libgen_search import *
from helpers import Helpers


class Basic_Search():
    """Create an ordinary json of the Ebook """

    def book_title(self, title):
        """provides json of a book

        Args:
            title ([name]): [name of the book]

        Returns:
            [json]: [data of the book]
        """
        # download_link = LibgenSearch().resolve_download_links(data)
        return LibgenSearch().search_title(title)

    def author_name(self, name):
        """search book by name of the author

        Args:
            name ([str]): [author of the book]

        Returns:
            [json]: [books by the author]
        """
        return LibgenSearch().search_author(name)

class filter_bs():
    """ customizing the filter 
    fuction in libgen api """

    def book_title(self, title, filters, ex_mt):
        """get library of books by specific matched

        Args:
            title ([str]): [title of the book]
            filters ([dic]): [the filters:filter.txt]
            ex_mt (bool, optional): [exact match of the filter]. Defaults to False.

        Returns:
            [json]: [data of a specific book or books]
        """
        return LibgenSearch().search_title_filtered(
            title, filters, exact_match=ex_mt)


    def author_name(name, filters, ex_mt):
        """same as above except name of th ebook is replaced with name of the author"""
        return LibgenSearch().search_author_filtered(
            name, filters, exact_match=ex_mt)
