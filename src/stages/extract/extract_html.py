from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.drivers.interfaces.http_collector import HtmlCollectorInterface
from src.drivers.interfaces.http_requester import HttpRequesterInterface


class ExtractHtml:
    def __init__(self, init_http_requester: HttpRequesterInterface,
                 init_html_collector: HtmlCollectorInterface) -> None:
        self.__http_requester = init_http_requester
        self.__html_collector = init_html_collector

    def extract(self):
        html_information = self.__http_requester.request_from_page()

        essential_information = self.__html_collector.collect_essential_information(html_information)

        ret = essential_information

        return ret