from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester
from src.stages.extract.extract_html import ExtractHtml
from src.stages.load.load_data import LoadData
from src.stages.transform.transform_raw_data import TransformRawData

http_requester = HttpRequester()
html_collector = HtmlCollector()

# E – Extract
extract_html = ExtractHtml(http_requester, html_collector)
extract_html_data = extract_html.extract()

# T – Transform
transform_raw_data = TransformRawData()
transform_html_data = transform_raw_data.transform(extract_html_data)

# L – Load
load_data = LoadData()
load_data.load(transform_html_data)
