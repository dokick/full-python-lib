"""This could be a single file library"""

from argparse import ArgumentParser


def get_message(verbose_flag: bool) -> str:
    """Returns a message

    :param bool verbose_flag: verbose flag
    :return: a message
    :rtype: str
    """
    if verbose_flag:
        return "Verbose flag activated"
    return "Verbose flag deactivated"


def add_one(number: float) -> float:
    """Adds one to given number

    :param float number: number
    :return: incremented number
    :rtype: float
    """
    return number + 1


def main() -> None:
    """Entry point for CLI"""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    print(get_message(args.verbose))


if __name__ == "__main__":
    main()
