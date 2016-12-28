# Runemetrics API

A quick n' dirty wrapper around the (unofficial) [Runemetrics](https://apps.runescape.com/runemetrics/app/welcome) API to get detailed player statistics in Runescape.

Requires users to provide username and password if you want to login.

## Usage

Two ways to use this:

- Unauthenticated:
```python
from runemetrics.player import Player

player = Player.fetch('player_name')

print(player.name)
print(player.levels['Agility'].level)
print(player.quests_complete)
```

```python
from runemetrics.player import Player

player = Player.login_and_fetch('username', 'password')

print(player.name)
# Only accessible after login
print(player.play_time)
```

To run the example:

```
$ python3 -m runemetrics get-profile <username> <password>
...
$ python3 -m runemetrics get-player <player_name>
```

## Motivation

I wanted to get my character's information to compare against other datasources (namely seeing how many of a certain monster I needed to kill to level up) and the capability didn't seem to exist.

## Installation

    $ pip install -r requirements.txt

## License

[MIT](LICENSE)
