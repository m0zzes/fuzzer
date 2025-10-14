from fuzzer.core import Fuzzer
import argparse
import logging
LOGGER = logging.getLogger(__name__)

json_example = """
{
    "url" : "http://example.com/FUZZ"
}
"""

argument_parser = argparse.ArgumentParser(
    prog="Fuzzer",
    description="Simple Website fuzzer written in Python",
    epilog="Author: Matyas Barocsai"
)

argument_parser.add_argument(
    "-u",
    "--url",
    help="Url to the target site, may contain FUZZ variables",
    type=str,
    required=False
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
    action="store_true",
    required=False,
)

argument_parser.add_argument(
    "-x",
    "--json_example",
    help="Prints an example json configuration file",
    default=False,
    action="store_true",
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

def clt():

    # Setup standard logger for CLT
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    args = argument_parser.parse_args()

    # If example arguments is set, then we show example and quit
    if args.json_example:
        LOGGER.info(json_example)
        return

    # Tool only works when either a config is passed or url argument is present
    if (not args.url) and (not args.json):
        LOGGER.info("Neither --url or --json was provided ")
        return

    # Verbose = Debug-mode
    if args.verbose:
        LOGGER.setLevel(logging.DEBUG)

    # Set output file for logging
    if args.output:
        logging.basicConfig(filename=args.output)

    # Parse comma-separated wordlists argument
    if args.wordlists is not None:
        args.wordlists = [w.strip() for w in args.wordlists.split(",")]

    # TODO: Use correct fields or change them in the core-program
    fuzzer = Fuzzer({
        "url" : args.url,
        "header" : args.header,
        "wordlists" : {

        },
        "options" : {
            "verbose" : args.verbose,
            "pool_size" : 4,
            "N": 1000
        }
    })

if __name__ =="__main__":
    clt()