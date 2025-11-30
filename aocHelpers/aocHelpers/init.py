import argparse
import logging
from os import path


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input", type=int, default=1, nargs="?", help="input file number"
    )
    parser.add_argument(
        "--log",
        "-l",
        default="info",
        choices=["debug", "info", "warn", "error"],
    )
    return parser


def init_logging(level):
    logging.basicConfig(
        level=level.upper(),
        format="[%(levelname)s] %(message)s",
    )


def init(dirpath, args=None):
    parser = get_arg_parser()
    pargs = parser.parse_args(args)

    init_logging(pargs.log)

    # determine input file
    filename = path.join(dirpath, f"input{pargs.input}.txt")
    logging.info(f"Using input: {filename}")

    with open(filename) as f:
        return f.read()
