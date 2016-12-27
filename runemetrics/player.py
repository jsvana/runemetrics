"""
Contains abstractions around some of the Runemetrics API
"""
import requests


class Level(object):
    """
    Represents a level in the Runemetrics API
    """

    LEVEL_XP = [
        0,
        83,
        174,
        276,
        388,
        512,
        650,
        801,
        969,
        1154,
        1358,
        1584,
        1833,
        2107,
        2411,
        2746,
        3115,
        3523,
        3973,
        4470,
        5018,
        5624,
        6291,
        7028,
        7842,
        8740,
        9730,
        10824,
        12031,
        13363,
        14833,
        16456,
        18247,
        20224,
        22406,
        24815,
        27473,
        30408,
        33648,
        37224,
        41171,
        45529,
        50339,
        55649,
        61512,
        67983,
        75127,
        83014,
        91721,
        101333,
        111945,
        123660,
        136594,
        150872,
        166636,
        184040,
        203254,
        224466,
        247886,
        273742,
        302288,
        333804,
        368599,
        407015,
        449428,
        496254,
        547953,
        605032,
        668051,
        737627,
        814445,
        899257,
        992895,
        1096278,
        1210421,
        1336443,
        1475581,
        1629200,
        1798808,
        1986068,
        2192818,
        2421087,
        2673114,
        2951373,
        3258594,
        3597792,
        3972294,
        4385776,
        4842295,
        5346332,
        5902831,
        6517253,
        7195629,
        7944614,
        8771558,
        9684577,
        10692629,
        11805606,
        13034431,
    ]

    LEVEL_NAMES = [
        'Attack',
        'Defence',
        'Strength',
        'Constitution',
        'Ranged',
        'Prayer',
        'Magic',
        'Cooking',
        'Woodcutting',
        'Fletching',
        'Fishing',
        'Firemaking',
        'Crafting',
        'Smithing',
        'Mining',
        'Herblore',
        'Agility',
        'Thieving',
        'Slayer',
        'Farming',
        'Runecrafting',
        'Hunter',
        'Construction',
        'Summoning',
        'Dungeoneering',
        'Divination',
        'Invention',
    ]

    def __init__(self, obj):
        self.level_id = obj['id']
        self.level = obj['level']
        self.experience = obj['xp'] / 10
        self.name = self.LEVEL_NAMES[self.level_id]

    @classmethod
    def level_experience(cls, level):
        """
        Gets the minimum required XP for a given level
        """
        return cls.LEVEL_XP[level - 1]

    @property
    def experience_to_next_level(self):
        """
        Gets the XP required to reach the next level
        """
        return self.level_experience(self.level + 1) - self.experience


class Player(object):
    """
    Represents a player in the Runemetrics API
    """

    LOGIN_URL = 'https://secure.runescape.com/m=weblogin/login.ws'
    PROFILE_URL = 'https://apps.runescape.com/runemetrics/profile/profile'

    def __init__(self, session, obj):
        self.session = session

        self.combat_level = obj['combatlevel']
        self.name = obj['name']
        self.playtime = obj['playtimedays'] + obj['playtimehours'] / 24
        self.quests_complete = obj['questscomplete']
        self.quests_started = obj['questsstarted']
        self.quests_not_started = obj['questsnotstarted']
        self.rank = int(obj['rank'].replace(',', ''))
        self.total_skill = obj['totalskill']
        self.total_experience = obj['totalxp'] / 10
        levels = [Level(l) for l in obj['skillvalues']]
        self.levels = {l.name: l for l in levels}

    @classmethod
    def login_and_fetch(cls, username, password):
        """
        Login to Runemetrics and fetch the player's data
        """
        session = requests.Session()
        session.post(
            cls.LOGIN_URL,
            data={
                'username': username,
                'password': password,
                'mod': 'www',
                'ssl': '0',
                'dest': 'community',
            },
        )
        return cls(session, session.get(cls.PROFILE_URL).json())
