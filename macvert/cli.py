#!/usr/bin/python

# cli.py - cli front end to program

import argparse
import os
import sys

sys.path += [os.path.abspath('..')]
from macvert.mac_operations import Operations

# Handle command line args
parser = argparse.ArgumentParser(description='Process some mac addresses.', formatter_class=argparse.RawTextHelpFormatter)
subparsers = parser.add_subparsers()

# Cli args
cli_p = subparsers.add_parser('cli')	
cli_p.set_defaults(which='cli')
cli_p.add_argument('-m', '--mac-addresses', nargs='+',
		help='Enter one or more mac addresses' +
		'seperated by a space')
cli_p.add_argument('-f', '--file', type=argparse.FileType('r'), help='File containing mac addresses.')
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
server_p = subparsers.add_parser('server')
server_p.set_defaults(which='server')
server_p.add_argument('-p', '--port', nargs='?', default=5000, type=int)

args = parser.parse_args()

if args == ["cli]":
	print args	

# Check if mac addresses were entered on the cli or a file was passed
if args.mac_addresses:
	macs = args.mac_addresses
	for mac in macs:
		mac_op = Operations(mac, args.input_type, args.output_type)
		if len(macs) == 1:
			print(mac_op.get_mac())
		else:
			print(mac_op.get_mac(), end=" ")
elif args.file:
	macs = args.file.readlines()
	for mac in macs:
		mac_op = Operations(mac, args.input_type, args.output_type)
		if len(macs) == 1:
			print(mac_op.get_mac())
		else:
			print(mac_op.get_mac(), end=" ")
elif args.port:
	app.run()	
