import json
from get_cover_links import get_cover_link
from libgen_api import LibgenSearch


def store_book(dict, bk_name):
    """stores a dic in a json file."""

    with open(f"ebook_json/{bk_name}.json", "w") as file:
        json.dump(dict, file, indent=4)
        print("Finished Processing")


def render_bk(dict, bk_name):
    """Tk results and add some import keys to the dictionary."""


    # delete x frm e dict
    for all_dict in dict:
        # print(f"Processing : {all_dict['ID']}")

        # Retrieve cover nd download link
        mirror_1 = get_cover_link(all_dict["Mirror_1"])
        dwn_link = LibgenSearch().resolve_download_links(all_dict)

        all_dict["dwn_link"] = dwn_link
        all_dict["Mirror_1"] = mirror_1
        del all_dict["Edit"],all_dict["Mirror_2"],all_dict["Mirror_3"],all_dict["Mirror_4"]
        # del all_dict["Mirrow_2"]
        # Now del unwanted keys from dic
        # for keys in x:
        # if set(x).issubset(all_dict):

        #     for a in x:
        #         del all_dict[a]
    return dict
