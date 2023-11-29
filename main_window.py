from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction
from qt_material import QtStyleTools

from components.app_table.app_table import AppTable
from data_base.db_engine import DataBaseEngine
from dataclass.page import Page
from enums.page_enum import PageEnum


class MainWindow(QMainWindow, QtStyleTools):
    _toolbar: QToolBar = None

    def __init__(self, db: DataBaseEngine = None):
        super(MainWindow, self).__init__()
        self.db = db

        self.resize(800, 600)

        self.set_right_menu_panel()
        self.set_main_menu()

    def set_right_menu_panel(self):
        self._toolbar = QToolBar('Вкладки', self)
        for enum in PageEnum:
            page: Page = enum.value
            setattr(self, page.get('name'), QAction(page.get('alias'), self))
            getattr(self, page.get('name')).triggered.connect(partial(self.load_window, page.get('name')))
            self._toolbar.addAction(getattr(self, page.get('name')))

        self.addToolBar(Qt.LeftToolBarArea, self._toolbar)
        menu_bar = self.menuBar()

    def set_main_menu(self):
        pass
        # file_menu = menu_bar.addMenu('&Сформировать')
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
        self.Window = AppTable(table_name=args[0], db=self.db)
        self.setCentralWidget(self.Window)
        self.show()
