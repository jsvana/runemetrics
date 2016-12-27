# Runemetrics API

A quick n' dirty wrapper around the (unofficial) [Runemetrics](https://apps.runescape.com/runemetrics/app/welcome) API to get detailed player statistics in Runescape.

Requires users to provide username and password to login.

## Usage

```python
from runemetrics.player import Player

player = Player.login_and_fetch('username', 'password')

print(player.name)
print(player.levels['Agility'].level)
print(player.quests_complete)
```

To run the example:

```
$ python3 -m runemetrics <username> <password>
gravsmasher - level 84
Name             Current Level    XP to Next Level
-------------  ---------------  ------------------
Constitution                65            25140.70
Hunter                      31               34.80
Woodcutting                 79           108886.00
Smithing                    52            12310.40
Crafting                    46             5780.30
...
```

## Motivation

I wanted to get my character's information to compare against other datasources (namely seeing how many of a certain monster I needed to kill to level up) and the capability didn't seem to exist.

## Installation

    $ pip install -r requirements.txt

## License

[MIT](LICENSE)
