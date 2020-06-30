#!/usr/bin/python

# mac_convertor.py - Converts mac address from various formats to other formats

import argparse
from macvert.mac_operations import Operations

def main():
	""" Main function of program """

	# Handle command line args
	parser = argparse.ArgumentParser(description='Process some mac addresses.', formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-m', '--mac-addresses', nargs='+',
			help='Enter one or more mac addresses' +
			'seperated by a space')
	parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='File containing mac addresses.')
	parser.add_argument('-i', '--input-type', required=True, 
			help='''
	Type of mac address notation the input is in.

	The mac address types are:
		- colon
		- hp
		- no_delimiter
		- dash
		''')
	parser.add_argument('-o', '--output-type', required=True, 
			help='''
	Type of mac address notation you want the mac address in.

	The mac address types are:
		- colon
		- hp
		- no_delimiter
		- dash
		''')
	args = parser.parse_args()

	# Check if mac addresses were entered on the cli or a file was passed
	if args.mac_addresses:
		macs = args.mac_addresses
	elif args.file:
		macs = args.file.readlines()

	for mac in macs:
		mac_op = Operations(mac, args.input_type, args.output_type)
		if len(macs) == 1:
			print(mac_op.get_mac())
		else:
			print(mac_op.get_mac(), end=" ")


if __name__ == '__main__':
    	main()
