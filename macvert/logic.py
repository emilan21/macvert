"""Batch conversion for the CLI and web adapter."""

from macvert.mac_operations import Operations


def convert_mac(macs, input_type, output_type):
    return [Operations(mac, input_type, output_type).get_mac() for mac in macs]
