from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox

import edit_window
import loop
import mainWindow


class TableWidget(QTableWidget):
    def __init__(self, lis):
        self.button_count = lis[-1]
        self.list = lis
        super().__init__(0, len(list(lis)) - 1)
        self.HeaderLabels = list(lis)[:-self.button_count - 1]
        for y in range(len(self.HeaderLabels), (len(self.HeaderLabels) + self.button_count)):
            self.HeaderLabels.append('')
        self.setHorizontalHeaderLabels(self.HeaderLabels)
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

    def removeItemRow(self, row=0):
        if self.rowCount() > 0:
            if row == 0:
                self.removeRow(self.rowCount() - 1)
            if row > 0:
                self.removeRow(row - 1)
            if row < 0:
                self.removeRow(self.rowCount() - row)

    def insertItem(self, item):
        if len(item) == self.columnCount() - self.button_count:
            self.insertRow(self.rowCount())
            rowCount = self.rowCount()
            columnCount = self.columnCount() - self.button_count
            for j in range(columnCount):
                cell = QTableWidgetItem()
                if type(item[j]) is float:
                    item[j] = round(item[j], 4)
                else:
                    pass
                cell.setText(str(item[j]))
                self.setItem(rowCount - 1, j, cell)
                if rowCount % 2 != 0:
                    cell.setBackground(QtGui.QColor(224, 224, 209))
            self.addButtons(rowCount, columnCount)

    def addButtons(self, rowCount, columnCount):
        RC = rowCount
        CC = columnCount
        for j in range(CC, self.columnCount()):
            But = QtWidgets.QPushButton()
            self.setCellWidget(RC - 2, j, But)
            But.setIconSize(QSize(25, 25))
            But.setIcon(QIcon(self.list[j]))
            But.clicked.connect(
                lambda *args, row=RC, column=j: self.controllButtons(row - 1, column))

    def controllButtons(self, Row, Colum):
        print(Row, " ", Colum)

    def clearTable(self):
        while self.rowCount() > 0:
            self.removeRow(self.rowCount() - 1)

    def getRowData(self, row):
        data = []
        for i in range(len(self.HeaderLabels) - self.button_count):
            data.append(self.item(row, i).text())
        return data


# controllButtons for "Search for product tab"
class Search(TableWidget):
    def controllButtons(self, Row, Colum):
        data = self.getRowData(Row - 1)
        if Colum == 9:
            msg = "هل ترغب في مسح هذا المنتج؟ " + data[1]
            msgbox = QMessageBox(QMessageBox.Question, "مسح منتج", msg)
            msgbox.setDefaultButton(QMessageBox.Cancel)
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msgbox.exec_()
            if retval == QMessageBox.Ok:
                mainWindow.db.execute("delete from 'shop' where ID = ? and NAME = ?", [data[0], data[1]])
                self.removeItemRow(Row)
                for rows in range(self.rowCount() + 1):
                    self.addButtons(rows, self.columnCount() - self.button_count)
        elif Colum == 8:
            self.EditPage = edit_window.EditWindow(data)
            self.EditPage.show()
            try:
                loop.loop.exec_()
            except:
                pass
        else:
            pass


# controllButtons for "sell Item tab"
class sellTab(TableWidget):
    def controllButtons(self, Row, Colum):
        # delete item
        if Colum == 9:
            self.removeItemRow(Row)
            for rows in range(self.rowCount() + 1):
                self.addButtons(rows, self.columnCount() - self.button_count)
            mainWindow.MainWindow.TD.removeData(Row - 1)
            self.addTotal()
            if self.rowCount() == 1:
                self.clearTable()
        # increase item
        elif Colum == 7:
            mainWindow.MainWindow.TD.increase(Row - 1)
            self.editValues(Row)
            self.addTotal()
        # decrease item
        elif Colum == 8:
            mainWindow.MainWindow.TD.decrease(Row - 1)
            if mainWindow.MainWindow.TD.getData(Row - 1)["sellCount"] <= 0:
                self.controllButtons(Row, 9)
            else:
                self.editValues(Row)
                self.addTotal()

    def editValues(self, Row):
        self.item(Row - 1, 3).setText(str(mainWindow.MainWindow.TD.getData(Row - 1)["sellCount"]))
        self.item(Row - 1, 5).setText(str(mainWindow.MainWindow.TD.getData(Row - 1)["profit"]))

    def addTotal(self):
        self.removeItemRow()
        totalProducts = 0
        totalPrice = 0
        for product in mainWindow.MainWindow.TD.getData():
            totalProducts += product["sellCount"]
            totalPrice += product["profit"]
        self.insertItem(["الاجمالي", "", "", totalProducts, "", totalPrice, ""])
