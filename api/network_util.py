import enum
from typing import Optional

import requests


class NetworkMethod(enum.Enum):
    GET = 1
    POST = 2
    PUT = 3


class NetworkUtil:
    @staticmethod
    def request(url: str, params: Optional[any], method: NetworkMethod):
        if method == NetworkMethod.GET:
            return requests.get(url, params=params)
        elif method == NetworkMethod.POST:
            return requests.post(url, params=params)
        elif method == NetworkMethod.PUT:
            return requests.put(url, params=params)
