from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class TableWidget(QTableWidget):
    def __init__(self, lis):
        self.button_count = lis[-1]
        self.list = lis
        super().__init__(0, len(list(lis))-1)
        self.HeaderLabels = list(lis)[:-self.button_count-1]
        self.setHorizontalHeaderLabels(self.HeaderLabels)
        self.verticalHeader().setVisible(False)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.setStyleSheet("font: 16px bold")

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

    def removeItemRow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount()-1)

    def insertItem(self, item):
        if len(item) == self.columnCount()-self.button_count:
            self.insertRow(self.rowCount())
            rowCount = self.rowCount()
            columnCount = self.columnCount()-self.button_count
            for j in range(columnCount):
                cell = QTableWidgetItem()
                cell.setText(str(item[j]))
                self.setItem(rowCount - 1, j, cell)
                if rowCount % 2 != 0:
                    cell.setBackground(QtGui.QColor(224, 224, 209))
            for j in range(columnCount, self.columnCount()):
                But = QtWidgets.QPushButton()
                self.setCellWidget(rowCount - 2, j, But)
                But.setIconSize(QSize(25, 25))
                But.setIcon(QIcon(self.list[j]))
                But.clicked.connect(
                    lambda *args, row=rowCount, column=j: self._findPlace(row, column))

    def _findPlace(self,Row,Colum):
        print(Row," ",Colum)
        # print(self.item(Row,))


    def clearTable(self):
        while self.rowCount() > 0:
            self.removeRow(self.rowCount()-1)

