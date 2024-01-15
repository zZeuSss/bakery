from enum import Enum

from database.data_controller import DataController
from dataclass.page import Page
from enums.page_type_enum import PageTypeEnum
from models.consumer import Consumer
from models.document import Document
from models.order import Order
from models.price import Price
from models.product import Product


class PageEnum(Enum):
    ORDER: Page = dict(
        name='order',
        alias='Заказы',
        type=PageTypeEnum.DATABASE.value,
        data_controller=DataController(model=Order)
    )
    CONSUMER: Page = dict(
        name='consumer',
        alias='Заказчики',
        type=PageTypeEnum.DATABASE.value,
        data_controller=DataController(model=Consumer)
    )
    PRODUCT: Page = dict(
        name='product',
        alias='Позиции',
        type=PageTypeEnum.DATABASE.value,
        data_controller=DataController(model=Product)
    )
    PRICE: Page = dict(
        name='price',
        alias='Цены',
        type=PageTypeEnum.DATABASE.value,
        data_controller=DataController(model=Price),
    )
    DOCUMENT: Page = dict(
        name='document',
        alias='Накладные',
        type=PageTypeEnum.DATABASE.value,
        data_controller=DataController(model=Document)
    )
    RESULT: Page = dict(
        name='result',
        alias='Итог',
        type=PageTypeEnum.OTHER.value,
        # data_controller=DataController(model=Result)
    )
