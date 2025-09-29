from fuzzer.core import Fuzzer

"""
    
    Intended usage.
    
    fuzzer --numbers /path --host example.com/FUZZ
    fuzzer --numbers /path,/path,/path --host example.com/FUZZ/FUZZ/FUZZ
    fuzzer --json /path
    

"""

if __name__ == "__main__":
    config = {
        "host" : "example.com/{F1}/test/{F1}",
        "headers" : {},
        "wordlists" : {
            "F1" : "/home/god/git/fuzzer/tests/numbers",
            "F2": "/home/god/git/fuzzer/tests/numbers"
        }
    }
    fuzzer = Fuzzer(config)


    print(fuzzer.get_host_testcases(10))