#!/usr/bin/python

# logic.py
import os
import sys

sys.path += [os.path.abspath('..')]
from macvert.mac_operations import Operations

def convert_mac(macs, input_type, output_type):
	for mac in macs:
		mac_op = Operations(mac, input_type, output_type)
		new_mac = mac_op.get_mac()
		return new_mac
