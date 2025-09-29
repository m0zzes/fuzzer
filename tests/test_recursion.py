import math

class Tester:

    def __init__(self, paths: list[str]):

        self.wordlists = []
        for p in paths:
            self.wordlists.append(self._read_file(p))


    def test_cases_n(self, start_index: int, n: int):

        r = []
        for i in range(start_index, start_index + n):
            result = self.test_case(i)
            if not result:
                break

            r.append(result)

        return r

    def test_case(self, start_index: int):

        indexes = []
        for i, wordlist in enumerate(self.wordlists):

            if i == len(wordlist) - 1:
                indexes.append((start_index % len(wordlist)) - 1)
            else:
                indexes.append(start_index // math.prod([len(w) for w in self.wordlists[i+1::]]))

        result = ""
        for i, wordlist in enumerate(self.wordlists):
            result += wordlist[indexes[i]]

        if start_index != 0 and result == self.test_case(0):
            return ""

        return result

    @staticmethod
    def _read_file(path: str) -> list[str]:

        data = []
        with open(path, 'r') as ifile:
            data = ifile.readlines()

        return [l.strip() for l in data]

if __name__ == "__main__":

    t = Tester([
        "/home/god/git/fuzzer/tests/alphabet",
        "/home/god/git/fuzzer/tests/alphabet",
        "/home/god/git/fuzzer/tests/alphabet",
        "/home/god/git/fuzzer/tests/alphabet"
    ])

    c1 = t.test_cases_n(0, 10)
    c2 = t.test_cases_n(100000000, 10)

    print("")