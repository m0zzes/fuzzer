from fuzzer.http_handlers.http_handler import HttpHandler

import asyncio
import aiohttp

class AioHttpHandler(HttpHandler):

    def run(self):
        asyncio.run(self.async_run())

    async def async_run(self):

        self.start_timer()

        async with aiohttp.ClientSession() as session:

            for fuzzing_table in self.fuzzing_tables:
                host = self._host(fuzzing_table)
                headers = self._headers(fuzzing_table)
                async with session.head(url=host, headers=headers) as response:
                    print(f"{host} - {response.status}")

        self.end_timer()