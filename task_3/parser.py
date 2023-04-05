import requests
from json import dumps


url = "https://www.python.org/"

response = requests.get(url=url)

text = response.text


def get_unique_pairs():
    unique_pairs = {}

    for elem in text:
        unique_pairs[elem] = text.count(elem)

    return unique_pairs


def write_file(json_data):
    with open("readme.md", "w") as file_handler:
        file_handler.write(dumps(json_data, indent=4))


if __name__ == "__main__":
    write_file(get_unique_pairs())
