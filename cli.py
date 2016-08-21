import argparse
from server import Daemon
from client import Client
import pdb

VERSION = "0.1"
DEFUALT_PORT = 6789

EXAMPLE =\
"""
Examples:
listen as server: cli.py -d [127.0.0.1] [8000]
connect to a server: cli.py -H 1.2.3.4 [-p 8000] [5.6.7.8] [9000]

%(prog)s {VERSION}
""".format(VERSION=VERSION)

arg_parser = argparse.ArgumentParser(
    prog="punchhole",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="cli for punchhole",
    epilog=EXAMPLE + "alkaid"
)

mutual_group = arg_parser.add_mutually_exclusive_group(required=True)
mutual_group.add_argument("-d", "--daemon", action="store_true", help="run as a daemon")
mutual_group.add_argument("-H", type=str, help="remote host")

arg_parser.add_argument("-P", type=int, default=DEFUALT_PORT, help="remote port")
arg_parser.add_argument("host", type=str, nargs="?", default='', help="use to a particular local addr")
arg_parser.add_argument("port", type=int, nargs="?", default=DEFUALT_PORT, help="use a particular local port")
arg_parser.add_argument("-v", "--version", action="version", version="%(prog)s " + VERSION)

args = arg_parser.parse_args()
print(args)

if args.daemon:
    server = Daemon(args.host, args.port)
    server.listen()
else:
    client = Client(args.host, args.port)
    client.punch((args.H, args.P))
