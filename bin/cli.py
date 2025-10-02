from fuzzer.core import Fuzzer

"""
    
    Intended usage.
    
    fuzzer --numbers /path --host example.com/FUZZ
    fuzzer --numbers /path,/path,/path --host example.com/FUZZ/FUZZ/FUZZ
    fuzzer --json /path
    

"""

if __name__ == "__main__":
    config = {
        "host" : "example.com/{F1}/{F2}/{F3}",
        "headers" : {},
        "wordlists" : {
            "F1" : "/home/god/git/fuzzer/tests/alphabet",
            "F2": "/home/god/git/fuzzer/tests/alphabet",
            "F3": "/home/god/git/fuzzer/tests/alphabet"
        }
    }
    fuzzer = Fuzzer(config)

    r = fuzzer.parse_n_test_cases(10000, 1000)

    for case in r:
        print(fuzzer.parse_host_argument(case))