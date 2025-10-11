from fuzzer.http_handlers.http_handler import HttpHandler
import requests

class RequestsHandler(HttpHandler):

    def run(self):

        self.start_timer()

        for fuzzing_table in self.fuzzing_tables:
            host = self._host(fuzzing_table)
            headers = self._headers(fuzzing_table)

            response = requests.head(url=host, headers=headers)
            self.report_response(response.status_code, host)

        self.end_timer()


    def run_one(self, fuzzing_table: dict):

        self.start_timer()

        host = self._host(fuzzing_table)
        headers = self._headers(fuzzing_table)

        response = requests.head(url=host, headers=headers)
        self.report_response(response.status_code, host)

        self.end_timer()