import requests


class HttpRequester:
    __url: str

    def __int__(self):
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    def request_from_page(self):
        print(self.__url)

        response = requests.get(self.__url)

        return {
            "status_code": response.status_code,
            "html": response.text
        }
