from typing import TypedDict, Optional

from database.data_controller import DataController


class Page(TypedDict, total=False):
    name: str
    alias: str
    type: str
    data_controller: Optional[DataController]
