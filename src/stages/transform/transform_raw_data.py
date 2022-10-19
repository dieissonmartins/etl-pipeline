from typing import List, Dict

from src.stages.contracts.extract_contract import ExtractContract


class TransformRawData:

    def transform(self, extract_contract: ExtractContract):
        try:
            ret = self.__filter_and_transform_data(extract_contract)
            return ret
        except Exception as e:
            raise TypeError(e)

    def __filter_and_transform_data(self, extract_contract: ExtractContract) -> List[Dict]:
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_information_content

        transformed_information = []

        for data in data_content:

            link = data['link']

            if 'artistid=' not in link:
                continue

            if ', ' in data['name']:
                names = data['name'].split(' ')
            elif ' ' in data['name']:
                names = data['name'].split(' ')
            else:
                names = [data['name']]

            transformed_data = self.__transform_data(names, link)
            transformed_data['transformed_date'] = extraction_date

            transformed_information.append(transformed_data)

        ret = transformed_information

        return ret

    def __transform_data(self, names: List, link: str) -> Dict:
        link_splited = link.split('artistid=')

        if len(names) == 2:
            aux = {
                "first_name": names[1],
                "second_name": names[0],
                "surname": None,
                "artist_id": link_splited[1],
                "link": link
            }
        elif len(names) == 3:
            aux = {
                "first_name": names[2],
                "second_name": names[0],
                "surname": names[1],
                "artist_id": link_splited[1],
                "link": link
            }
        else:
            aux = {
                "first_name": names[0],
                "second_name": None,
                "surname": None,
                "artist_id": link_splited[1],
                "link": link
            }

        ret = aux

        return ret
