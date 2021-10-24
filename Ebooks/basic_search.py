import json
import time
from .crawlers.libgen_search import LibgenSearch as lb


class Basic_Search():
    """Return an ebook in json format """

    def book_title(self, title):
        """provides json of a book

        Args:
            title ([name]): [name of the book]

        Returns:
            [json]: [data of the book]
        """
        # download_link = LibgenSearch().resolve_download_links(data)
        return lb().search_title(title)


    def author_name(self, name):
        """search book by name of the author

        Args:
            name ([str]): [author of the book]

        Returns:
            [json]: [books by the author]
        """
        return lb().search_author(name)

    def filter_title(self, title, filters, ex_mt=True):
        """get library of books by specific matched

        Args:
            title ([str]): [title of the book]
            filters ([dic]): [the filters:filter.txt]
            ex_mt (bool, optional): [exact match of the filter]. Defaults to False.

        Returns:
            [json]: [data of a specific book or books]
        """
        return lb().search_title_filtered(
            title, filters, exact_match=ex_mt)


    def filter_author(self,name, filters, ex_mt):
        """same as above except name of th ebook is replaced with name of the author"""
        return lb().search_author_filtered(
        name, filters, exact_match=ex_mt)



class Advance_Search():
    """Add download links and cover links to the search result"""
    def book_title(self, title):
        """provides json of a book

        Args:
            title ([name]): [name of the book]

        Returns:
            [json]: [data of the book]
        """

        x = lb().search_title(title)  
        return lb().resolve_download_links(x)

    def author_name(self, name):
        """search book by name of the author

        Args:
            name ([str]): [author of the book]

        Returns:
            [json]: [books by the author]
        """
        result = lb().search_author(name)
        return lb().resolve_download_links(result)


    def filter_title(self, title, filters, ex_mt=True):
        """get library of books by specific matched

        Args:
            title ([str]): [title of the book]
            filters ([dic]): [the filters:filter.txt]
            ex_mt (bool, optional): [exact match of the filter]. Defaults to False.

        Returns:
            [json]: [data of a specific book or books]
        """
        return lb().search_title_filtered(
            title, filters, exact_match=ex_mt)


    def filter_author(self,name, filters, ex_mt):
        """same as above except name of th ebook is replaced with name of the author"""
        return lb().search_author_filtered(
            name, filters, exact_match=ex_mt)


