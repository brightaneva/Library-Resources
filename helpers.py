import json


def store_data(result, json_name):
    """stores a dic in a json file."""

    with open(f"data/{json_name}.json", "w") as file:
        json.dump(result, file, indent=4)
        print("Finished Processing")

