"""
Contains abstractions around the Beastiary API
"""


import requests


class Beast(object):

    BEAST_URL = (
        'http://services.runescape.com/m=itemdb_rs'
        '/bestiary/beastData.json?beastid={beast_id}'
    )
    SEARCH_URL = (
        'http://services.runescape.com/m=itemdb_rs'
        '/bestiary/beastSearch.json?term={query}'
    )

    def __init__(self, obj):
        for key, value in obj.items():
            setattr(self, key, value)

    @classmethod
    def search(cls, query):
        r = requests.get(cls.SEARCH_URL.format(query=query))
        for result in r.json():
            yield result['value'], result['label']

    @classmethod
    def get(cls, beast_id):
        r = requests.get(cls.BEAST_URL.format(beast_id=beast_id))
        return Beast(r.json())
