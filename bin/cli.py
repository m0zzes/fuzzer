import argparse

argument_parser = argparse.ArgumentParser(
    prog="Fuzzer",
    description="Simple Website fuzzer written in Python",
    epilog="Author: Matyas Barocsai"
)

argument_parser.add_argument(
    "url",
    help="Url to the target site, may contain FUZZ variables",
    type=str
)

argument_parser.add_argument(
    "-j",
    "--json",
    help="Json configuration containing all the arguments",
    type=argparse.FileType("r")
)

argument_parser.add_argument(
    "-H",
    "--header",
    help="Custom header to use in the requests, may contain FUZZ variables",
    default={},
    required=False
)

argument_parser.add_argument(
    "-w",
    "--wordlists",
    help="Wordlists to use when fuzzing, comma-separated list",
    default="",
    type=str,
    required=False
)

argument_parser.add_argument(
    "-V",
    "--verbose",
    help="Log extra output for debugging",
    default=False,
    type=bool,
    required=False
)

argument_parser.add_argument(
    "-o",
    "--output",
    help="Output logs and results in a file",
    default=False,
    type=argparse.FileType("w"),
    required=False
)


if __name__ =="__main__":
    args = argument_parser.parse_args()

    # Parse comma-separated wordlists argument
    if args.wordlists is not None:
        args.wordlists = [w.strip() for w in args.wordlists.split(",")]