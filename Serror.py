from PyQt5 import QtCore, QtWidgets

import demo_mode


class Ui_support_error(object):
    def setupUi(self, support_error):
        self.support_error = support_error
        self.support_error.setObjectName("support_error")
        self.support_error.resize(650, 125)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.support_error.sizePolicy().hasHeightForWidth())
        self.support_error.setSizePolicy(sizePolicy)
        self.support_error.setMinimumSize(QtCore.QSize(650, 0))
        self.support_error.setMaximumSize(QtCore.QSize(650, 16777215))
        self.centralwidget = QtWidgets.QWidget(self.support_error)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QGridLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 200 15pt ;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, 0, 1, 1)
        self.meme = QtWidgets.QWidget()
        self.meme.setSizePolicy(sizePolicy)
        self.meme.setMinimumSize(QtCore.QSize(400, 200))
        self.meme.setMaximumSize(QtCore.QSize(650, 300))
        self.meme.setStyleSheet(
            "background-image: url(meme.jpg);background-repeat: no-repeat;background-position: center;opacity: 0.5")
        self.verticalLayout.addWidget(self.meme, 1, 0, 1, 1)
        self.memeTxt = QtWidgets.QLabel()
        self.memeTxt.setText("هو يدعم بس لازم تشتريه نيهاهاهاها")
        self.verticalLayout.addWidget(self.memeTxt, 2, 0, 1, 1, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

        self.demo = QtWidgets.QPushButton(self.centralwidget)
        self.demo.setObjectName("demo")
        self.demo.clicked.connect(self.showDemo)
        self.verticalLayout.addWidget(self.demo, 3, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.support_error.setCentralWidget(self.centralwidget)
        self.retranslateUi(self.support_error)
        QtCore.QMetaObject.connectSlotsByName(self.support_error)

    def retranslateUi(self, support_error):
        _translate = QtCore.QCoreApplication.translate
        support_error.setWindowTitle(_translate("support_error", "support_error"))
        self.label.setText(
            _translate("support_error", "للاسف جهازك لا يدعم تشغيل هذا البرنامج برجاء التواصل مع الشركه"))
        self.demo.setText(_translate("support_error", "تجربه النسخه المجانيه"))

    def showDemo(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = demo_mode.demoWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.retranslateUi(self.MainWindow)
        self.MainWindow.show()
        self.support_error.hide()
