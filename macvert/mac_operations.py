#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


# mac_operations.py - Class that preforms operations on the mac address.
class Operations(object):
    """ Mac operations class """

    def __init__(self, mac_address, input_type, output_type):
        self.mac_address = mac_address
        self.input_type = input_type
        self.output_type = output_type

# Get mac address in a standard notation

    def normalize(self):
        if self.input_type == 'colon':

            return self.mac_address
        if self.input_type == 'hp':
            split_list = re.split('-', self.mac_address)
            first_string = split_list[0]
            second_string = split_list[1]
            thrid_string = split_list[2]
            octet_1 = first_string[0] + first_string[1] + ':'
            octet_2 = first_string[2] + first_string[3] + ':'
            octet_3 = second_string[0] + second_string[1] + ':'
            octet_4 = second_string[2] + second_string[3] + ':'
            octet_5 = thrid_string[0] + thrid_string[1] + ':'
            octet_6 = thrid_string[2] + thrid_string[3]

            return octet_1 + octet_2 + octet_3 + octet_4 + octet_5 + octet_6
        if self.input_type == 'no_delimiter':
            n = 2
            new = [
                self.mac_address[i:i + n]
                for i in range(0, len(self.mac_address), n)
            ]

            return new[0] + ":" + new[1] + ":" + new[2] + ":" + new[
                3] + ":" + new[4] + ":" + new[5]
        if self.input_type == 'dash':
            split_list = re.split('-', self.mac_address)

            return split_list[0] + ':' + split_list[1] + ':' + split_list[
                2] + ':' + split_list[3] + ':' + split_list[
                    4] + ':' + split_list[5]

    # Convert the mac address to output type
    def convert_mac(self, normalized_mac):
        if self.output_type == 'colon':
            return normalized_mac
        if self.output_type == 'hp':
            split_list = re.split(':', normalized_mac)

            return split_list[0] + split_list[1] + '-' + split_list[
                2] + split_list[3] + '-' + split_list[4] + split_list[5]
        if self.output_type == 'no_delimiter':
            split_list = re.split(':', normalized_mac)

            return split_list[0] + split_list[1] + split_list[2] + split_list[
                3] + split_list[4] + split_list[5]
        if self.output_type == 'dash':
            split_list = re.split(':', normalized_mac)

            return split_list[0] + '-' + split_list[1] + '-' + split_list[
                2] + '-' + split_list[3] + '-' + split_list[
                    4] + '-' + split_list[5]

    # Return final mac address back to caller
    def get_mac(self):

        return self.convert_mac(self.normalize())
