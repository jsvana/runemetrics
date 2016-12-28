"""
Example usage of and wrapper around the Runemetrics API
"""
import argparse
import math
import sys


from tabulate import tabulate


from .beastiary import Beast
from .player import (
    AuthenticationError,
    Player,
)


def parse_args():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    profile_parser = subparsers.add_parser(
        'get-profile',
        help="Get your profile's information",
    )
    profile_parser.add_argument(
        'username',
        help='Account username',
    )
    profile_parser.add_argument(
        'password',
        help='Account password',
    )
    profile_parser.set_defaults(function=cmd_get_profile)

    player_parser = subparsers.add_parser(
        'get-player',
        help="Get a public player's information",
    )
    player_parser.add_argument(
        'name',
        help='Name of player to get',
    )
    player_parser.set_defaults(function=cmd_get_player)

    return parser.parse_args()


def cmd_get_profile(args):
    try:
        player = Player.login_and_fetch(
            args.username,
            args.password,
        )
    except AuthenticationError as e:
        print('Unable to load player: {}'.format(e), file=sys.stderr)
        return False

    attack = player.levels['Attack']
    print(player.name, attack.experience)

    return True


def cmd_get_player(args):
    try:
        player = Player.fetch(args.name)
    except AuthenticationError as e:
        print('Unable to load player: {}'.format(e), file=sys.stderr)
        return False

    attack = player.levels['Attack']
    print(player.name, attack.experience)

    return True

def main():
    args = parse_args()
    return args.function(args)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
