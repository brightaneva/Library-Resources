import json
import time
from .search_request import SearchRequest
from .libgen_search import LibgenSearch
from .helpers import store_book


class BS():
    """Create an ordinary json of the Ebook """

    def book_title(self, title):
        """provides json of a book

        Args:
            title ([name]): [name of the book]

        Returns:
            [json]: [data of the book]
        """
        return LibgenSearch().search_title(title)

    def author_name(self, name):
        """search book by name of the author

        Args:
            name ([str]): [author of the book]

        Returns:
            [json]: [books by the author]
        """
        return LibgenSearch().search_author(name)


class Filter_BS():
    """ customizing the filter 
    fuction in libgen api """

    def book_title(self, title, filters, ex_mt=False):
        """get library of books by specific matched

        Args:
            title ([str]): [title of the book]
            filters ([dic]): [the filters:filter.txt]
            ex_mt (bool, optional): [exact match of the filter]. Defaults to False.

        Returns:
            [json]: [data of a specific book or books]
        """
        lg_filter = LibgenSearch().search_title_filtered(
            title, filters, exact_match=ex_mt)

        if ex_mt == 'True':
            lg_filter = LibgenSearch().search_title_filtered(
                title, filters, exact_match=True)

        return lg_filter


    def author_name(name, filters, ex_mt=False):
        """same as above except name of th ebook is replaced with name of the author"""
        # self.name 
        lg_filter = LibgenSearch().search_author_filtered(
            name, filters, exact_match=ex_mt)

        if ex_mt == 'True':
            lg_filter = LibgenSearch().search_author_filtered(
                name, filters, exact_match=True)

        return lg_filter
