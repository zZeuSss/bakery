from dataclasses import dataclass
from typing import List


@dataclass
class Column:
    key: str
    header: str


@dataclass
class TableConfig:
    key: str
    columns: List[Column]
