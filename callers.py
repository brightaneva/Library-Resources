import json

def store_book(dict, bk_name):
    """stores a dic in a json file."""

    with open(f"data/{bk_name}.json", "w") as file:
        json.dump(dict, file, indent=4)
        print("Finished Processing")