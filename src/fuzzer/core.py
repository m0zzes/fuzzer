import math

class Fuzzer:

    def __init__(self, config: dict):
        self.config = config
        self.wordlists: list[tuple[str, str]] = self._read_wordlists()

    def _get_single_test_case(self, index: int = 0) -> list[int]:
        """Returns a single test-case based on the wordlists. A testcase is a list of indexes (integer) for a
        combination of words from the wordlists.
        """

        indexes = []
        rest: int = index
        for i, wordlist_tup in enumerate(self.wordlists):
            if i == len(self.wordlists) - 1:
                indexes.append(index % len(wordlist_tup[1]))
            else:
                prod = math.prod([len(v) for k,v in self.wordlists[i+1::]])
                indexes.append(rest // prod)
                rest = rest % prod

        return indexes

    def _get_n_test_cases(self, start_index: int = 0, n: int = 10) -> list[list[int]]:
        """Returns n number of testcases (default=10) from start index (default=0)
        """

        result = []
        for i in range(start_index, start_index + n):
            test_case = self._get_single_test_case(i)
            result.append(test_case)

        return result

    def parse_n_test_cases(self, index: int, n: int = 1) -> list[dict[str, str]]:
        """Parses the indexes of n test-cases at index, breaks if indexes are out-of-range
        """

        test_cases: list[list[int]] = self._get_n_test_cases(index, n)
        result = []
        for test_case in test_cases:
            fuzzing_table = {}
            for i, wordlist_tup in enumerate(self.wordlists):
                try:
                    fuzzing_table[wordlist_tup[0]] = wordlist_tup[1][test_case[i]]
                except IndexError:
                    return result

            result.append(fuzzing_table)

        return result

    def _read_wordlists(self) -> list[tuple[str, str]]:
        """Reads all the wordlists and stores them together with the corresponding Fuzz-key
        """

        result = []
        for fuzz_key, wordlist_path in self.config.get("wordlists", {}).items():
            with open(wordlist_path, "r") as ifile:
                result.append(('{' + fuzz_key + '}', [l.strip() for l in ifile.readlines()]))

        return result

    def parse_host_argument(self, fuzzing_table: dict) -> str:
        """
        """

        result = self.config["host"]
        for fuzz_key, fuzz_value in fuzzing_table.items():
            result = result.replace(fuzz_key, fuzz_value)

        return result