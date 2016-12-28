"""
Example usage of and wrapper around the Runemetrics API
"""
import math
import sys


from tabulate import tabulate


from .beastiary import Beast
from .player import Player


def main():
    if len(sys.argv) != 3:
        print(
            'Usage: {} <username> <password>'.format(sys.argv[0]),
            file=sys.stderr,
        )
        sys.exit(1)

    player = Player.login_and_fetch(sys.argv[1], sys.argv[2])
    attack = player.levels['Attack']

    for beast_id, name in Beast.search('Lesser Demon'):
        beast = Beast.get(beast_id)

        if beast.experience == 0:
            continue
        beasts_left = math.ceil(
            attack.experience_to_next_level / beast.experience
        )

        print(
            '{} {}s left until level {} ({:.2f} xp left, {} per)'.format(
                beasts_left,
                name,
                attack.level + 1,
                attack.experience_to_next_level,
                beast.experience
            )
        )


if __name__ == "__main__":
    main()
