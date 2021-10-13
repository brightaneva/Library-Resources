import json
import time
from .search_request import SearchRequest
from .libgen_search import LibgenSearch
from .get_cover_links import get_cover_link
from .helpers import render_bk


class RS():

    def book_title(self,title):
        """provides json of a book

        Args:
            title ([name]): [name of the book]

        Returns:
            [json]: [data of the book]
        """
        self.title = title
        result = LibgenSearch().search_title(self.title)

        #render_bk take 2args, adds essential keys
        #and return json
        return render_bk(result, self.title)

    def author_name(self, name):
        """same as above except name of th ebook is replaced with name of the author"""
        self.name = name
        result = LibgenSearch().search_author(self.name)

        return render_bk(result,self.name)


class Filter_RS():
    """
    Add needed keys to 
    a filter search.
    """

    def book_title(self, title, filters, ex_mt=False):
        self.title = title
        lg_filter = LibgenSearch().search_title_filtered(
                title, filters, exact_match=ex_mt)

        if ex_mt == 'True':
            lg_filter = LibgenSearch().search_title_filtered(
                title, filters, exact_match=True)

        #render_bk take 2args
        #adds essential keys
        #and return json
        return render_bk(lg_filter, self.title)

    def author_name(self, name, filters, ex_mt=False):
        """same as above except name of th ebook is replaced with name of the author"""
        self.name = name
        lg_filter = LibgenSearch().search_author_filtered(
            name, filters, exact_match=ex_mt)

        if ex_mt == 'True':
            lg_filter = LibgenSearch().search_author_filtered(
                name, filters, exact_match=True)

        return render_bk(lg_filter,self.name)