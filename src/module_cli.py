from __future__ import annotations

import argparse
from io import TextIOWrapper
from typing import NoReturn
from typing import Sequence


__version__ = "22.4.1"  # module-cli version

MODULE_S = """\
from __future__ import annotations

import argparse
from typing import NoReturn
from typing import Sequence


__version__ = "0.1.0"


def cli(args: Sequence[str] | None = None) -> NoReturn:
    raise SystemExit(main(args))


def main(args: Sequence[str] | None = None) -> int | str:
    parser = create_parser()
    ns = parser.parse_args(args)
    debug: bool = ns.debug

    try:
        return ns.handler(ns)
    except Exception as e:
        if debug:
            raise
        else:
            return str(e)


def create_parser(
    parser: argparse.ArgumentParser | None = None,
) -> argparse.ArgumentParser:
    parser = parser or argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "-D",
        "--debug",
        action="store_true",
        default=False,
        help="run program in debug mode",
    )

    # ---------------------------------
    # CONFIGURE COMMAND-LINE ARGUGMENTS
    # ---------------------------------

    parser.set_defaults(handler=handler)

    return parser


def handler(ns: argparse.Namespace) -> int:
    # -----------------
    # ADD PROGRAM LOGIC
    # -----------------
    print("Hello, World!")

    return 0


if __name__ == "__main__":
    cli()
"""


def cli() -> NoReturn:
    raise SystemExit(main())


def main(args: Sequence[str] | None = None) -> int | str:
    parser = create_parser()
    ns = parser.parse_args(args)
    debug: bool = ns.debug

    try:
        return ns.handler(ns)
    except Exception as e:
        if debug:
            raise
        else:
            return str(e)


def create_parser(
    parser: argparse.ArgumentParser | None = None,
) -> argparse.ArgumentParser:
    description = "Bootstrap a single-module python CLI"
    parser = parser or argparse.ArgumentParser(description=description)
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "-D",
        "--debug",
        action="store_true",
        default=False,
        help="run program in debug mode",
    )
    parser.add_argument(
        "out",
        type=argparse.FileType("w"),
        nargs="?",
        default="-",
        help="File to write to. (default: %(default)s)",
    )

    parser.set_defaults(handler=handler)

    return parser


def handler(ns: argparse.Namespace) -> int:
    out: TextIOWrapper = ns.out
    out.write(MODULE_S)

    return 0


if __name__ == "__main__":
    cli()
