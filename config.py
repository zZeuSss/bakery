import os

DB_TYPE_CONNECTION = 'sqlite'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/source'


PAGES_TABLE_HEADERS = {
    'order': ['№', 'Наименование', 'Cумма', 'Счет', 'Комментарий'],
    'consumer': ['№', 'Наименование', 'Телефон', 'Почта', 'Способ оплаты', 'Комментарий'],
    'price': ['№', 'Товар', 'Цена'],
    'product': ['№', 'Наименование', 'Граммы'],
    'document': ['№', 'Наименование', 'Скачать']
}
