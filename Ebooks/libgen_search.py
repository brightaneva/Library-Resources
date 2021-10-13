from .search_request import SearchRequest
import requests
from bs4 import BeautifulSoup

MIRROR_SOURCES = ["GET"]


class LibgenSearch():
    def search_title(self, query):
        search_request = SearchRequest(query, search_type="title")
        return search_request.aggregate_request_data()

    def search_author(self, query):
        search_request = SearchRequest(query, search_type="author")
        return search_request.aggregate_request_data()

    def search_title_filtered(self, query, filters, exact_match=True):
        return self._extracted_from_search_author_filtered_2(
            query, "title", filters, exact_match
        )

    def search_author_filtered(self, query, filters, exact_match=True):
        return self._extracted_from_search_author_filtered_2(
            query, "author", filters, exact_match
        )

    # TODO Rename this here and in `search_title_filtered` and `search_author_filtered`
    def _extracted_from_search_author_filtered_2(self, query, search_type, filters, exact_match):
        search_request = SearchRequest(query, search_type=search_type)
        results = search_request.aggregate_request_data()
        return filter_results(
            results=results, filters=filters, exact_match=exact_match
        )

    def resolve_download_links(self, item):
        # delete x frm e dic
        mirror_1 = item["Mirror_1"]
        page = requests.get(mirror_1)
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all("a", string=MIRROR_SOURCES)
        return {link.string: link["href"] for link in links}


def filter_results(results, filters, exact_match):
    """
    Returns a list of results that match the given filter criteria.
    When exact_match = true, we only include results that exactly match the filters (ie. the filters are an exact subset of the result).
    When exact-match = false, we run a case-insensitive check between each filter field and each result.

    exact_match defaults to TRUE - this is to maintain consistency with older versions of this library.
    """

    filtered_list = []
    if exact_match:
        for result in results:
            # check whether a candidate result matches the given filters
            if filters.items() <= result.items():
                filtered_list.append(result)

    else:
        filter_matches_result = False
        for result in results:
            for field, query in filters.items():
                if query.casefold() in result[field].casefold():
                    filter_matches_result = True
                else:
                    filter_matches_result = False
                    break
            if filter_matches_result:
                filtered_list.append(result)
    return filtered_list
