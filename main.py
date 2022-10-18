from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester
from src.stages.extract.extract_html import ExtractHtml

http_requester = HttpRequester()
html_collector = HtmlCollector()

# E – Extract
extract_html = ExtractHtml(http_requester, html_collector)
res = extract_html.extract()

# T – Transform

# L – Load
