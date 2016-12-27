"""
Example usage of and wrapper around the Runemetrics API
"""
import sys


from tabulate import tabulate


from .player import Player


def main():
    if len(sys.argv) != 3:
        print(
            'Usage: {} <username> <password>'.format(sys.argv[0]),
            file=sys.stderr,
        )
        sys.exit(1)

    player = Player.login_and_fetch(sys.argv[1], sys.argv[2])

    print('{} - level {}'.format(player.name, player.combat_level))

    rows = []
    for level in player.levels.values():
        rows.append([
            level.name,
            level.level,
            level.experience_to_next_level,
        ])

    print(
        tabulate(
            rows,
            headers=['Name', 'Current Level', 'XP to Next Level'],
            numalign='right',
            floatfmt='.2f',
        )
    )


if __name__ == "__main__":
    main()
