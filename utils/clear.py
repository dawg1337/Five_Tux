from utils import banner

import os

""" Clear handeling for various distro's """

def clear_with_banner():
    if os == 'nt':
        os.system('cls')
        banner.FiveTux()

    else:
        os.system('cls')
        banner.FiveTux()


def clear():
    if os == 'nt':
        os.system('cls')

    else:
        os.system('cls')
