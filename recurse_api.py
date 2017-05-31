#!/usr/bin/python3
import requests
import json
from sys import argv
from sys import exit

def recurse_api(START="", END="", count=0):

    count += 1
    if count > 10:
        return (search_dict)
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': "query",
        'format': "json",
        'prop': "links",
        'titles': START,
        'pllimit': "max"
    }
    search_dict = {}
    r = requests.get(base_url, params=params)
    print(r.status_code)
    unpack_json = r.json().get('query').get('pages')
    list_of_pages = list(unpack_json.keys())[0]
    unpack_json = unpack_json.get(list_of_pages).get('links')

    for item in unpack_json:
        if END in item or END == item:
            return (search_dict)
        else:
            recurse_api(item.get('title'), END, count)
        search_dict.update({count : item.get('title')})
        print(item.get('title'))

    with open(START, 'w') as f:
        f.write(json.dumps(r.json()))



if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ./recurse_api.py <Start point> <End goal>")
        exit(1)
    page_url = "https://en.wikipedia.org/wiki/" + argv[1]
    print(recurse_api(argv[1], argv[2], 0))
