from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QListWidget, QAbstractItemView, \
    QHBoxLayout, QListWidgetItem

from database.db_engine import DataBaseEngine
from database.models import Consumer


class OrderDialog(QDialog):
    def __init__(self, parent=None, db: DataBaseEngine = None):
        super().__init__(parent)
        self.db = db
        self.data = []
        self.setWindowTitle('Заказчики')
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.button_box = QDialogButtonBox(QBtn)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        v_order_lay = QVBoxLayout()

        self.order_select = QListWidget(self)
        self.order_select.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setValues(self.order_select)

        v_order_lay.addWidget(QLabel('Заказ', self))
        v_order_lay.addWidget(self.order_select)

        v_bonus_lay = QVBoxLayout()

        self.bonus_select = QListWidget(self)
        self.bonus_select.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setValues(self.bonus_select)

        v_bonus_lay.addWidget(QLabel('Бонус', self))
        v_bonus_lay.addWidget(self.bonus_select)

        v_trade_lay = QVBoxLayout()

        self.trade_select = QListWidget(self)
        self.trade_select.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setValues(self.trade_select)

        v_trade_lay.addWidget(QLabel('Обмен', self))
        v_trade_lay.addWidget(self.trade_select)

        hlay = QHBoxLayout()

        hlay.addLayout(v_order_lay)
        hlay.addLayout(v_bonus_lay)
        hlay.addLayout(v_trade_lay)

        vlay = QVBoxLayout()
        vlay.addLayout(hlay)
        vlay.addWidget(self.button_box)

        self.setLayout(vlay)

    def setValues(self, list: QListWidget):
        for consumer in self.db.list(Consumer):
            item = QListWidgetItem()
            item.setData(0, consumer)
            item.setText(consumer.name)
            list.addItem(item)

    def accept(self):
        self.data = {
            'order': [item for item in self.order_select.selectedItems()],
            'bonus': [item for item in self.bonus_select.selectedItems()],
            'trade': [item for item in self.trade_select.selectedItems()],
        }
        return super().accept()
