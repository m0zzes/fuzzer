import copy
import re

class Element:

    def __init__(self, value: str):
        self.value: str = value

    def get(self) -> str:
        return self.value

class FuzzElement(Element):

    def __init__(self, value: str, wordlist: list[str]):
        super().__init__(value)
        self.index = 0
        self.wordlist: list[str] = wordlist

    def get(self) -> str:
        word = self.wordlist[self.index].strip()
        self.index += 1
        return word

class Fuzzer:

    def __init__(self, config: dict):
        self.config = config

        self.wordlists: dict[str, list] = {}
        self.read_wordlists()

        self.host_fuzz_array = self.parse_string_into_elements(self.config.get("host"))

    def get_host_testcases(self, n = 10) -> list[str]:

        result = []

        for i in range(n):
            result.append("".join([fuzz_elem.get() for fuzz_elem in self.host_fuzz_array]))

        return result

    def read_wordlists(self) -> None:

        for fuzz_key, wordlist_path in self.config.get("wordlists", {}).items():
            with open(wordlist_path, "r") as ifile:
                self.wordlists['{' + fuzz_key + '}'] = ifile.readlines()

    def parse_string_into_elements(self, string: str) -> list[Element]:

        result = []

        fuzz_variables = re.findall(pattern=r"{F\d+}", string=string)

        tmp_string: str = string
        for i, fuzz_variable in enumerate(fuzz_variables):

            if fuzz_variable not in tmp_string:
                break

            segments = tmp_string.split(fuzz_variable)

            # intersperse fuzz variables in the elements list
            tmp_elements = [Element(s) for s in segments]
            elements = [FuzzElement(fuzz_variable, self.wordlists[fuzz_variable])] * (len(tmp_elements) * 2 - 1)
            elements[0::2] = tmp_elements

            if elements[-1].value == "" or i != (len(fuzz_variables) - 1):
                elements.pop(-1)

            result.extend(elements)

            # Continue searching for more fuzz_variables in the rest of the string
            tmp_string = segments[-1]

        return result
