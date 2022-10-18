from typing import Dict
from .interfaces.http_requester import HttpRequesterInterface
import requests


class HttpRequester(HttpRequesterInterface):
    __url: str

    #def __int__(self) -> None:
    #    self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    def request_from_page(self) -> Dict[str, str | int]:
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

        response = requests.get(self.__url)

        ret = {
            "status_code": response.status_code,
            "html": response.text
        }

        return ret
