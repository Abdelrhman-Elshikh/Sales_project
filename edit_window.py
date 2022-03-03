from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

import mainWindow
import loop



class EditWindow(QtWidgets.QMainWindow):
    def __init__(self, dataList):
        super().__init__()
        self.id = dataList[0]
        self.name = dataList[1]
        self.type = dataList[2]
        self.itemNumber = float(dataList[3])
        self.sellprice = float(dataList[6])
        self.buyprice = float(dataList[4])
        self.halfprice = float(dataList[5])
        self.resize(500, 344)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setVerticalSpacing(20)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.itemName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemName.sizePolicy().hasHeightForWidth())
        self.itemName.setSizePolicy(sizePolicy)
        self.itemName.setMaximumSize(QtCore.QSize(16777215, 50))
        self.itemName.setObjectName("itemName")
        self.itemName.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_8.addWidget(self.itemName, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(13)
        self.label.setMidLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 1, 1, 1)
        self.codeGrid = QtWidgets.QGridLayout()

        self.codelabel = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codelabel.sizePolicy().hasHeightForWidth())
        self.codelabel.setSizePolicy(sizePolicy)
        self.codelabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.codelabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.codelabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.codelabel.setLineWidth(13)
        self.codelabel.setMidLineWidth(0)
        self.codelabel.setTextFormat(QtCore.Qt.AutoText)
        self.codelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.codelabel.setIndent(0)
        self.codelabel.setObjectName("codelabel")
        self.codelabel.setText("الكود")
        self.codeGrid.addWidget(self.codelabel,0,1,1,1)
        self.idText = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idText.sizePolicy().hasHeightForWidth())
        self.idText.setSizePolicy(sizePolicy)
        self.idText.setMaximumSize(QtCore.QSize(16777215, 50))
        self.idText.setObjectName("idText")
        self.idText.setAlignment(QtCore.Qt.AlignCenter)
        self.idText.setText(self.id)
        self.codeGrid.addWidget(self.idText, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.codeGrid, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 2, 1, 1)
        self.saveadding = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveadding.sizePolicy().hasHeightForWidth())
        self.saveadding.setSizePolicy(sizePolicy)
        self.saveadding.setMaximumSize(QtCore.QSize(16777215, 50))
        self.saveadding.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveadding.setObjectName("saveadding")
        self.gridLayout_7.addWidget(self.saveadding, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 4, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 9, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.sell = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sell.sizePolicy().hasHeightForWidth())
        self.sell.setSizePolicy(sizePolicy)
        self.sell.setMaximumSize(QtCore.QSize(16777215, 50))
        self.sell.setDecimals(2)
        self.sell.setMaximum(5000.99)
        self.sell.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.sell.setProperty("value", 0.0)
        self.sell.setObjectName("sellTab")
        self.gridLayout_13.addWidget(self.sell, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setLineWidth(13)
        self.label_5.setMidLineWidth(0)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.gridLayout_13.addWidget(self.label_5, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_13, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_11, 4, 0, 1, 1)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_10.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10.setLineWidth(13)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setIndent(0)
        self.label_10.setObjectName("label_10")
        self.gridLayout_22.addWidget(self.label_10, 0, 1, 1, 1)
        self.halfbuy = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.halfbuy.sizePolicy().hasHeightForWidth())
        self.halfbuy.setSizePolicy(sizePolicy)
        self.halfbuy.setMaximumSize(QtCore.QSize(16777215, 50))
        self.halfbuy.setMaximum(5000.99)
        self.halfbuy.setObjectName("halfbuy")
        self.gridLayout_22.addWidget(self.halfbuy, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_22, 6, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.number = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number.sizePolicy().hasHeightForWidth())
        self.number.setSizePolicy(sizePolicy)
        self.number.setMaximumSize(QtCore.QSize(16777215, 50))
        self.number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number.setMaximum(5000.99)
        self.number.setObjectName("number")
        self.gridLayout_10.addWidget(self.number, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(13)
        self.label_3.setMidLineWidth(0)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.gridLayout_10.addWidget(self.label_3, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_10, 3, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.itemType = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemType.sizePolicy().hasHeightForWidth())
        self.itemType.setSizePolicy(sizePolicy)
        self.itemType.setMaximumSize(QtCore.QSize(16777215, 50))
        self.itemType.setObjectName("itemType")
        self.itemType.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_9.addWidget(self.itemType, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(13)
        self.label_2.setMidLineWidth(0)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_9, 2, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.buy = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buy.sizePolicy().hasHeightForWidth())
        self.buy.setSizePolicy(sizePolicy)
        self.buy.setMaximumSize(QtCore.QSize(16777215, 50))
        self.buy.setMaximum(5000.99)
        self.buy.setObjectName("buy")
        self.gridLayout_12.addWidget(self.buy, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setLineWidth(13)
        self.label_4.setMidLineWidth(0)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.gridLayout_12.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_12, 5, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.saveadding.clicked.connect(self.saveedit)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("self", "اسم المنتج"))
        self.saveadding.setText(_translate("self", "حفظ"))
        self.label_5.setText(_translate("self", "سعر البيع"))
        self.label_10.setText(_translate("self", "سعر النص جمله"))
        self.label_3.setText(_translate("self", "الكميه او العدد"))
        self.label_2.setText(_translate("self", "النوع"))
        self.label_4.setText(_translate("self", "سعر الجمله "))
        self.itemName.setText(self.name)
        self.itemType.setText(self.type)
        self.number.setValue(self.itemNumber)
        self.sell.setValue(self.sellprice)
        self.buy.setValue(self.buyprice)
        self.halfbuy.setValue(self.halfprice)

    def saveedit(self):
        num = self.number.value()
        sellPrice = self.sell.value()
        buyPrice = self.buy.value()
        halfbuy = self.halfbuy.value()

        if sellPrice > 0 and buyPrice > 0 and sellPrice > buyPrice and halfbuy > 0 \
                and sellPrice >= halfbuy and halfbuy >= buyPrice:
            mainWindow.db.execute("UPDATE 'shop' set count = ? , BUY_PRICE = ? , HALF_PRICE = ? , SELL_PRICE = ? WHERE id = ?",[num,buyPrice,halfbuy,sellPrice,self.id])
            loop.loop.quit()

        elif sellPrice == 0 or buyPrice == 0 or halfbuy == 0 or sellPrice < buyPrice or sellPrice < halfbuy or halfbuy < buyPrice:
            self.label_5.setStyleSheet("color: red")
            self.label_4.setStyleSheet("color: red")
            self.label_10.setStyleSheet("color: red")
        else:
            self.label.setStyleSheet("color: red")
