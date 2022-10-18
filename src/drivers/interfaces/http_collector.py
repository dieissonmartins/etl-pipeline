from abc import ABC, abstractmethod
from typing import Any


class HtmlCollectorInterface(ABC):

    @abstractmethod
    def collect_essential_information(self, html) -> list[dict[str, str | Any]]:
        pass
