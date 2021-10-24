import json
import time
import requests
from bs4 import BeautifulSoup
from .search_request import SearchRequest
from .libgen_search import LibgenSearch
from .get_cover_links import get_cover_link
from .helper import render_bk


class RS():

    def book_title(self,title):
        """provides json of a book

        Args:
            title ([name]): [name of the book]

        Returns:
            [json]: [data of the book]
        """
        result = LibgenSearch().search_title(title)

        for all_dict in result:
            r = requests.get(all_dict["Mirror_1"])
            soup = BeautifulSoup(r.text, 'html.parser')
            images = soup.find_all('img')
            # img_link = f"http://library.lol{images['src']}"
            dwn_link = LibgenSearch().resolve_download_links(all_dict)

            all_dict["dwn_link"] = dwn_link
            all_dict["Book_cover"] = "img_link"


        return result


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