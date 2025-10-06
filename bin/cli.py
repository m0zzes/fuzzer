from fuzzer.core import Fuzzer
from fuzzer.http_handlers.requests_handler import RequestsHandler
from fuzzer.http_handlers.aiohttp_handler import AioHttpHandler

"""
    
    Intended usage.
    
    fuzzer --numbers /path --host example.com/FUZZ
    fuzzer --numbers /path,/path,/path --host example.com/FUZZ/FUZZ/FUZZ
    fuzzer --json /path
   
   
   
    FuzzEngine -> | RequestHandler <-> RequestObject | 
    

"""

if __name__ == "__main__":
    config = {
        "host" : "https://www.example.com/{F1}/{F2}",
        "headers" : {},
        "wordlists" : {
            "F1" : "/home/god/git/fuzzer/tests/numbers",
            "F2": "/home/god/git/fuzzer/tests/numbers"
        }
    }
    fuzzer = Fuzzer(config)

    fuzzing_tables = fuzzer.parse_n_test_cases(0, 100)

    # 78.76s execution time for 100 test cases (full request)
    # 77.80s execution time for 100 test cases (head only)
    rh = AioHttpHandler(
        host=config["host"],
        headers=config["headers"],
        fuzzing_tables=fuzzing_tables,
        filters=[]
    ).run()


    # 90.75s execution time for 100 test cases (head only)
    """
    rh2 = RequestsHandler(
        host=config["host"],
        headers=config["headers"],
        fuzzing_tables=fuzzing_tables,
        filters=[]
    ).run()
    """
