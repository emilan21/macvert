#!/usr/bin/python

# logic.py
from mac_operations import Operations


def convert_mac(macs, input_type, output_type):
    new_macs = []
    for mac in macs:
        mac_op = Operations(mac, input_type, output_type)
        new_macs.append(mac_op.get_mac())
    return new_macs
