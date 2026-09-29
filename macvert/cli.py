"""Command-line and optional Flask entry points."""

import argparse
import sys

from macvert.logic import convert_mac
from macvert.mac_operations import FORMATS


def main(argv=None):
    parser = argparse.ArgumentParser(description="Convert 48-bit MAC addresses")
    subparsers = parser.add_subparsers(dest="command", required=True)
    cli = subparsers.add_parser("cli", help="Convert addresses from arguments or a file")
    source = cli.add_mutually_exclusive_group(required=True)
    source.add_argument("-m", "--mac-addresses", nargs="+", metavar="MAC")
    source.add_argument("-f", "--file", type=argparse.FileType("r"))
    cli.add_argument("-i", "--input-type", choices=FORMATS, required=True)
    cli.add_argument("-o", "--output-type", choices=FORMATS, required=True)
    server = subparsers.add_parser("server", help="Start the optional Flask interface")
    server.add_argument("-p", "--port", default=5000, type=int)
    args = parser.parse_args(argv)

    if args.command == "server":
        from macvert.web import app

        app.run(host="127.0.0.1", port=args.port)
        return 0

    try:
        if args.file:
            with args.file:
                addresses = [line for line in args.file.read().splitlines() if line.strip()]
        else:
            addresses = args.mac_addresses
        print("\n".join(convert_mac(addresses, args.input_type, args.output_type)))
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
