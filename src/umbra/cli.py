"""Точка входа для командной строки."""

from __future__ import annotations

import argparse
import sys

from umbra import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="umbra",
        description="Offline photo verification toolkit for OSINT.",
    )
    parser.add_argument("--version", action="version", version=f"umbra {__version__}")
    parser.add_subparsers(dest="command", metavar="COMMAND")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
