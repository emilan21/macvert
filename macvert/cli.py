#!/usr/bin/python

# cli.py - cli front end to program

#from macvert.mac_operations import Operations
from mac_operations import Operations
import argparse
import os
import sys

sys.path += [os.path.abspath('..')]

# Handle command line args
parser = argparse.ArgumentParser(
    description='Process some mac addresses.',
     formatter_class=argparse.RawTextHelpFormatter)
subparser = parser.add_subparsers(help='Specify cli or server', dest='command')

# Cli args
cli_p = subparser.add_parser('cli', help='cli option for mac addresses on the cli')
cli_p.add_argument('-m', '--mac-addresses', nargs='+',
		help='Enter one or more mac addresses' +
		'seperated by a space')
cli_p.add_argument(
    '-f',
    '--file',
    type=argparse.FileType('r'),
     help='File containing mac addresses.')
cli_p.add_argument('-i', '--input-type', required=True,
		help='''
Type of mac address notation the input is in.

The mac address types are:
	- colon
	- hp
	- no_delimiter
	- dash
	''')
cli_p.add_argument('-o', '--output-type', required=True,
		help='''
Type of mac address notation you want the mac address in.

The mac address types are:
	- colon
	- hp
	- no_delimiter
	- dash
	''')

# Server args
server_p = subparser.add_parser('server', help='server option for running a web server to handle mac addreses')
server_p.add_argument('-p', '--port', nargs='?', default=5000, type=int)

args = parser.parse_args()
print(args)

if args.command == "cli":
    # Check if mac addresses were entered on the cli or a file was passed
    if args.mac_addresses:
         macs = args.mac_addresses
         for mac in macs:
             mac_op = Operations(mac, args.input_type, args.output_type)
             if len(macs) == 1:
                 print(mac_op.get_mac())
             else:
                 print(mac_op.get_mac(), end="\n")

    if args.file:
        macs = args.file.readlines()
        for mac in macs:
            mac_op = Operations(mac, args.input_type, args.output_type)
            if len(macs) == 1:
                print(mac_op.get_mac())
            else:
                print(mac_op.get_mac(), end="\n")

if args.command == "server":
    if args.port:
        app.run()	
