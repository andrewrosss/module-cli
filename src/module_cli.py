from __future__ import annotations

import argparse
from io import TextIOWrapper
from typing import NoReturn


__version__ = "1.0.0"  # module-cli version

MODULE_S = """\
from __future__ import annotations

import argparse
from typing import NoReturn


__version__ = "0.1.0"


def cli() -> NoReturn:
    raise SystemExit(main())


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()

    if hasattr(args, "handler"):
        return args.handler(args)

    parser.print_help()
    return 1


def create_parser(
    parser: argparse.ArgumentParser | None = None,
) -> argparse.ArgumentParser:
    parser = parser or argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="version", version=__version__)

    # ---------------------------------
    # CONFIGURE COMMAND-LINE ARGUGMENTS
    # ---------------------------------

    parser.set_defaults(handler=handler)

    return parser


def handler(args: argparse.Namespace) -> int:
    # ------------------
    # ADD BUSINESS LOGIC
    # ------------------
    print("Hello, World!")

    return 0


if __name__ == "__main__":
    cli()
"""


def cli() -> NoReturn:
    raise SystemExit(main())


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()

    if hasattr(args, "handler"):
        return args.handler(args)

    parser.print_help()
    return 1


def create_parser(
    parser: argparse.ArgumentParser | None = None,
) -> argparse.ArgumentParser:
    parser = parser or argparse.ArgumentParser()
    parser.add_argument(
        "out",
        type=argparse.FileType("w"),
        nargs="?",
        default="-",
        help="File to write to. (default: %(default)s)",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)

    parser.set_defaults(handler=handler)

    return parser


def handler(args: argparse.Namespace) -> int:
    out: TextIOWrapper = args.out
    out.write(MODULE_S)

    return 0


if __name__ == "__main__":
    cli()
