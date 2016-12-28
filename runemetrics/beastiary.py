"""
Contains abstractions around the Beastiary API
"""


import requests


class Beast(object):

    BEAST_URL = (
        'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json'
    )
    SEARCH_URL = (
        'http://services.runescape.com/m=itemdb_rs/bestiary/beastSearch.json'
    )

    def __init__(self, obj):
        for key, value in obj.items():
            setattr(self, key, value)
        self.experience = float(self.xp)

    @classmethod
    def search(cls, query):
        r = requests.get(
            cls.SEARCH_URL,
            params={
                'term': query,
            },
        )
        for result in r.json():
            yield result['value'], result['label']

    @classmethod
    def get(cls, beast_id):
        r = requests.get(
            cls.BEAST_URL,
            params={
                'beastid': beast_id,
            },
        )
        return Beast(r.json())
