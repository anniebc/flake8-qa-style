from typing import Optional

from flake8_plugin_utils import Visitor

from flake8_2gis_style.config import Config


class VisitorWithFilename(Visitor):
    filename: str

    def __init__(self, config: Optional[Config] = None,
                 filename: Optional[str] = None) -> None:
        super().__init__(config=config)
        self.filename = filename
