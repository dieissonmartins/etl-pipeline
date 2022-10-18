from typing import Any
from bs4 import BeautifulSoup
from src.drivers.interfaces.http_collector import HtmlCollectorInterface


class HtmlCollector(HtmlCollectorInterface):

    def collect_essential_information(self, html) -> list[dict[str, str | Any]]:
        html = html['html']

        soup = BeautifulSoup(html, features='html.parser')

        artist_name_list = soup.find(class_='BodyText')

        artist_name_list_items = artist_name_list.find_all('a')

        essential_information = []

        for artist_name in artist_name_list_items:
            names = artist_name.contents[0]
            links = 'https://web.archive.org' + artist_name.get('href')
            essential_information.append({
                "name": names,
                "link": links
            })

        ret = essential_information

        return ret
