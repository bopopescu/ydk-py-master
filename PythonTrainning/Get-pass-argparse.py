#!/usr/bin/env python

import argparse, getpass

class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass.getpass()

        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser('Test password parser')
parser.add_argument('-p', action=Password, nargs='?', dest='password', help='Enter your password')
args = parser.parse_args()

print args.password
