from enum import Enum

from dataclass.page import Page
from enums.page_type_enum import PageTypeEnum


class PageEnum(Enum):
    ORDER: Page = dict(
        name='order',
        alias='Заказы',
        type=PageTypeEnum.DATABASE.value
    )
    CONSUMER: Page = dict(
        name='consumer',
        alias='Заказчики',
        type=PageTypeEnum.DATABASE.value
    )
    PRODUCT: Page = dict(
        name='product',
        alias='Позиции',
        type=PageTypeEnum.DATABASE.value
    )
    PRICE: Page = dict(
        name='price',
        alias='Цены',
        type=PageTypeEnum.DATABASE.value
    )
    DOCUMENT: Page = dict(
        name='document',
        alias='Накладные',
        type=PageTypeEnum.DATABASE.value
    )
    RESULT: Page = dict(
        name='result',
        alias='Итог',
        type=PageTypeEnum.OTHER.value
    )
