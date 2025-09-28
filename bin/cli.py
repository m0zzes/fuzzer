from fuzzer.core import Fuzzer

"""
    
    Intended usage.
    
    fuzzer --wordlist /path --host example.com/FUZZ
    fuzzer --wordlist /path,/path,/path --host example.com/FUZZ/FUZZ/FUZZ
    fuzzer --json /path
    

"""

if __name__ == "__main__":
    config = {
        "host" : "example.com/{F1}/test/{F1}",
        "headers" : {},
        "wordlists" : {
            "F1" : "/home/god/git/fuzzer/tests/wordlist",
            "F2": "/home/god/git/fuzzer/tests/wordlist"
        }
    }
    fuzzer = Fuzzer(config)


    print(fuzzer.get_host_testcases(10))