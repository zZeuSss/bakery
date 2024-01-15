from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QMenuBar, QMenu
from qt_material import QtStyleTools

from dataclass.page import Page
from enums.page_enum import PageEnum
from views.table_view import TableView


class MainWindow(QMainWindow, QtStyleTools):
    _toolbar: QToolBar = None

    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(1920, 1020)

        self.set_left_menu_panel()
        self.set_main_menu()

    def set_left_menu_panel(self):
        self._toolbar = QToolBar('Вкладки', self)
        for enum in PageEnum:
            page: Page = enum.value
            setattr(self, page.get('name'), QAction(page.get('alias'), self))
            getattr(self, page.get('name')).triggered.connect(
                partial(self.load_window, page.get('data_controller')))
            self._toolbar.addAction(getattr(self, page.get('name')))

        self.addToolBar(Qt.LeftToolBarArea, self._toolbar)

    def set_main_menu(self):
        menu_bar = QMenuBar(self)

        # order_menu = QMenu("&Сформировать", self)
        #
        # order_action = QAction('&Заказ', self)
        # order_action.triggered.connect(self.order_dialog)
        # order_menu.addAction(order_action)

        maintainer_menu = QMenu("&Владелец", self)
        maintainer_menu.triggered.connect(self.order_dialog)

        # menu_bar.addMenu(order_menu)
        menu_bar.addMenu(maintainer_menu)

        self.setMenuBar(menu_bar)

    def load_window(self, *args):
        self.Window = TableView(data_controller=args[0])
        self.setCentralWidget(self.Window)
        self.show()

    def order_dialog(self):
        pass