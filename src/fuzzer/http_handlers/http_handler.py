import time

class HttpHandler:
    """Core HTTP Handler
    """

    def __init__(self, host: str, headers: dict, fuzzing_tables: list[dict], filters: list):
        self.host = host
        self.headers = headers
        self.fuzzing_tables = fuzzing_tables
        self.filters = filters

        # timing related variables
        self.start_time = -1
        self.end_time = -1
        self.run_time = -1

    def replace_fuzzing_keys(self, fuzzed_string: str, fuzzing_table: dict) -> str:
        """Replaces all fuzzing-keys with their corresponding value, given a fuzzing_table
        """

        result = fuzzed_string
        for fuzz_key, fuzz_value in fuzzing_table.items():
            result = result.replace(fuzz_key, fuzz_value)

        return result

    def _headers(self, fuzzing_table: dict) -> dict:
        """Returns a header dictionary, where all key/value pairs have been
        replaced with their corresponding fuzz-values
        """

        result = {}
        for key,value in self.headers.items():
            k = self.replace_fuzzing_keys(key, fuzzing_table)
            v = self.replace_fuzzing_keys(value, fuzzing_table)

            result[k] = v

        return result

    def _host(self, fuzzing_table: dict) -> str:
        """Returns the value of host given a fuzzing_tables
        """
        return self.replace_fuzzing_keys(self.host, fuzzing_table)

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self):
        self.end_time = time.time()
        self.run_time = self.end_time - self.start_time
        print(f"Execution time: {self.run_time}")

    def run(self):
        pass


