from typing import TypedDict


class Page(TypedDict, total=False):
    name: str
    alias: str
    type: str
