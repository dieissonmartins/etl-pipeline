from bs4 import BeautifulSoup


class HtmlCollector:

    def collect_essential_information(self, html: str):
        soup = BeautifulSoup(html, 'html.parser')

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