from fuzzer.core import Fuzzer
from fuzzer.http_handlers.requests_handler import RequestsHandler
from fuzzer.http_handlers.aiohttp_handler import AioHttpHandler

import time

# Threading
from multiprocessing import Pool

"""

    Intended usage.

    fuzzer --numbers /path --host example.com/FUZZ
    fuzzer --numbers /path,/path,/path --host example.com/FUZZ/FUZZ/FUZZ
    fuzzer --json /path



    FuzzEngine -> | RequestHandler <-> RequestObject | 


"""

if __name__ == "__main__":
    start_time = time.time()

    config = {
        "host": "http://hacknet.htb/{F1}",
        "options": {
            "verbose": True,
            "pool_size": 4,
            "N": 1000
        },
        "headers": {},
        "wordlists": {
            "F1": "/home/god/git/wordlists/wordlists/discovery/common.txt"
        }
    }

    pool_size: int = config["options"]["pool_size"]
    n: int = config["options"]["N"]

    fuzzer = Fuzzer(config)
    fuzzing_tables = fuzzer.parse_n_test_cases(0, n)

    handler = RequestsHandler(
        host=config["host"],
        options=config["options"],
        headers=config["headers"],
        fuzzing_tables=fuzzing_tables,
        filters=[]
    )

    with Pool(pool_size) as multipool:
        multipool.map(handler.run_one, fuzzing_tables)

    print(f"Execution time: {time.time() - start_time}s")