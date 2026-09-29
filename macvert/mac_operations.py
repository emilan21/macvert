"""Validated conversions among four common 48-bit MAC address notations."""

import re


FORMATS = {
    "colon": re.compile(r"(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\Z"),
    "hp": re.compile(r"[0-9A-Fa-f]{4}(?:-[0-9A-Fa-f]{4}){2}\Z"),
    "no_delimiter": re.compile(r"[0-9A-Fa-f]{12}\Z"),
    "dash": re.compile(r"(?:[0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}\Z"),
}


class Operations:
    def __init__(self, mac_address, input_type, output_type):
        self.mac_address = mac_address.strip()
        self.input_type = input_type
        self.output_type = output_type

    def normalize(self):
        pattern = FORMATS.get(self.input_type)
        if pattern is None:
            raise ValueError("Unknown input format: {}".format(self.input_type))
        if not pattern.fullmatch(self.mac_address):
            raise ValueError("Invalid {} MAC address: {}".format(self.input_type, self.mac_address))
        digits = self.mac_address.replace(":", "").replace("-", "")
        return ":".join(digits[index:index + 2] for index in range(0, 12, 2))

    def convert_mac(self, normalized_mac):
        if self.output_type not in FORMATS:
            raise ValueError("Unknown output format: {}".format(self.output_type))
        digits = normalized_mac.replace(":", "")
        if self.output_type == "no_delimiter":
            return digits
        width = 4 if self.output_type == "hp" else 2
        separator = ":" if self.output_type == "colon" else "-"
        return separator.join(digits[index:index + width] for index in range(0, 12, width))

    def get_mac(self):
        return self.convert_mac(self.normalize())
