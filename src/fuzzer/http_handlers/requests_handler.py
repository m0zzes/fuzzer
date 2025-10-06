from fuzzer.http_handlers.http_handler import HttpHandler
import requests

class RequestsHandler(HttpHandler):

    def run(self):

        self.start_timer()

        for fuzzing_table in self.fuzzing_tables:
            host = self._host(fuzzing_table)
            headers = self._headers(fuzzing_table)

            response = requests.head(url=host, headers=headers)
            print(f"{host} - {response.status_code}")

        self.end_timer()