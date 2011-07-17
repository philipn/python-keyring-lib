#!/usr/bin/env python
"""Simple command line interface to get/set password from a keyring"""

import getpass
import optparse
import sys

import keyring


def input_password(prompt):
    """Ask for a password to the user.

    This mostly exists to ease the testing process.
    """

    return getpass.getpass(prompt)


def output_password(password):
    """Output the password to the user.

    This mostly exists to ease the testing process.
    """

    print password


def main(argv=None):
    """Main command line interface."""

    parser = optparse.OptionParser(usage="%prog [get|set] SERVICE USERNAME")

    if argv is None:
        argv = sys.argv[1:]

    opts, args = parser.parse_args(argv)

    try:
        kind, service, username = args
    except ValueError:
        parser.error("Wrong number of arguments")

    if kind == 'get':
        password = keyring.get_password(service, username)
        if password is None:
            return 1

        output_password(password)
        return 0

    elif kind == 'set':
        password = input_password("Password for '%s' in '%s': " %
                                  (username, service))
        keyring.set_password(service, username, password)
        return 0

    else:
        parser.error("You can only 'get' or 'set' a password.")


if __name__ == '__main__':
    sys.exit(main())
