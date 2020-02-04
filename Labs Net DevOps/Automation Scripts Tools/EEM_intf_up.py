#Embedded Event Managment and Python

from cli import configurep
import argparse

#Retrieve the interface from command line using argparse

parser = argparse.argumentParser()
parser.add_argument("Interface IP", help="Interface to bring up")
args = parser.parse_args()

#list of command to argumentParser

command {"Interface {}".format(args.interface),
"no shut"}

#Run commands using Python API - COMMANDS NEED TO ME SEMICOLON SEPARATED

configurep(commands)
