from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction
from qt_material import QtStyleTools

from components.app_table.app_table import AppTable
from data_base.db_engine import DataBaseEngine
from config import PAGES


class MainWindow(QMainWindow, QtStyleTools):

    def __init__(self, db: DataBaseEngine = None):
        super(MainWindow, self).__init__()
        self.db = db
        # left toolbar
        toolbar = QToolBar('Вкладки', self)
        self.resize(800, 600)

        for page, name in PAGES:
            setattr(self, page, QAction(name, self))
            getattr(self, page).triggered.connect(partial(self.load_window, page))
            toolbar.addAction(getattr(self, page))

        self.addToolBar(Qt.LeftToolBarArea, toolbar)
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('&Сформировать')

        # self.add_menu_theme(self, self.menuStyles)

        # self.styles = QAction('Стили', self)
        # self.add_menu_theme(self, self.styles)

        # documents_action = QAction('&Накладные', self)
        # documents_action.triggered.connect(self.newDocument)
        # file_menu.addAction(documents_action)
        #
        # order_action = QAction('&Списки', self)
        # order_action.triggered.connect(self.newOrder)
        # file_menu.addAction(order_action)

        # self.setStyleSheet(pyqtcss.get_style("dark_orange"))


    def load_window(self, *args):
        self.Window = AppTable(table=args[0], db=self.db)
        self.setCentralWidget(self.Window)
        self.show()

    # def newDocument(self):
    #     pass
    #
    # def newOrder(self):
    #     dlg = OrderDialog(self, db=self.db)
    #     if dlg.exec():
    #         columns: List[Product] = self.db.session.query().with_entities(Product.name).all()
    #         df: pd.DataFrame = pd.DataFrame(
    #             columns=['Заказчики', 'Вид оплаты', 'Сумма', 'Количество', *[it.name for it in columns]]
    #         )
    #         df[[col for col in df.columns if col not in ['Заказчики', 'Вид оплаты']]].astype('int64', copy=False)
    #         df.fillna(value='', inplace=True)
    #         oder_df = pd.concat([df, pd.DataFrame(data=dlg.data.get('order'), columns=['Заказчики'])])
    #         bonus_df = pd.concat([df, pd.DataFrame(data=dlg.data.get('bonus'), columns=['Заказчики'])])
    #         trade_df = pd.concat([df, pd.DataFrame(data=dlg.data.get('trade'), columns=['Заказчики'])])
    #
    #         self.orders_page(
    #             order_df=oder_df,
    #             bonus_df=bonus_df,
    #             trade_df=trade_df
    #         )
    #
    #         self.setCentralWidget(self.Window)
    #         self.show()
    #
    # def newTrade(self):
    #     pass
    #
    # def newBonus(self):
    #     pass

    # def orders_page(
    #         self,
    #         *args,
    #         order_df: pd.DataFrame = None,
    #         bonus_df: pd.DataFrame = None,
    #         trade_df: pd.DataFrame = None,
    # ):
    #     self.Window = QTabWidget(self)
    #     self.Window.addTab(
    #         FileTable(
    #             self,
    #             business=Calculate,
    #             source='order.xlsx',
    #             data=order_df
    #         ),
    #         'Заказы'
    #     )
    #     self.Window.addTab(
    #         FileTable(
    #             self,
    #             business=Calculate,
    #             source='trade.xlsx',
    #             data=trade_df
    #         ),
    #         'Обмены'
    #     )
    #     self.Window.addTab(
    #         FileTable(
    #             self,
    #             business=Calculate,
    #             source='bonus.xlsx',
    #             data=bonus_df
    #         ),
    #         'Бонусы')
    #     self.setCentralWidget(self.Window)
    #     self.show()
    #
    # def consumers_page(self):
    #     self.Window = TableView(
    #         table=DataBaseTable(self, db=self.db, table='consumer')
    #     )
    #     self.setCentralWidget(self.Window)
    #     self.show()
    #
    # def product_page(self):
    #     self.Window = TableView(
    #         table=DataBaseTable(self, db=self.db, table='product')
    #     )
    #     self.setCentralWidget(self.Window)
    #     self.show()
    #
    # def price_page(self):
    #     self.Window = TableView(
    #         table=DataBaseTable(self, db=self.db, table='price')
    #     )
    #     self.setCentralWidget(self.Window)
    #     self.show()
    #
    # def document_page(self):
