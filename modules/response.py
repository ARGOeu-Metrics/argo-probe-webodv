import json

import requests
from argo_probe_webodv.exceptions import WarningException, CriticalException


class Analyse:
    def __init__(self, url, data, timeout):
        self.url = url
        self.data = data
        self.timeout = timeout

    def _fetch(self):
        # POST request with predefined data
        response = requests.post(
            self.url,
            data=json.dumps(self.data),
            headers={"Content-Type": "application/json"},
            timeout=self.timeout
        )

        # if status code is different from 2**, this will raise an exception
        response.raise_for_status()

        return response.json()

    def analyse(self):
        try:
            response = self._fetch()

            # checking if response json contains the given key: if not,
            # WarningException will be raised
            if not response["export_success"]:
                raise WarningException("Export not successful")

        # if any other exception is raised, it will call CriticalException
        except (
            requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.RequestException,
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects
        ) as e:
            raise CriticalException(e)
