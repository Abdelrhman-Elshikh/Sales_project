from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import mainWindow

class login(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'اغلاق', 'هل تريد الخروج',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            mainWindow.db.commit()
        else:
            event.ignore()

    def __init__(self):
        super().__init__()
        self.resize(669, 155)
        self.setMaximumSize(QtCore.QSize(16777215, 160))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, -1, 5, -1)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.user_name_lab = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_name_lab.sizePolicy().hasHeightForWidth())
        self.user_name_lab.setSizePolicy(sizePolicy)
        self.user_name_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name_lab.setObjectName("user_name_lab")
        self.gridLayout.addWidget(self.user_name_lab, 0, 0, 1, 1)
        self.user_name_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_name_input.sizePolicy().hasHeightForWidth())
        self.user_name_input.setSizePolicy(sizePolicy)
        self.user_name_input.setObjectName("user_name_input")
        self.gridLayout.addWidget(self.user_name_input, 0, 1, 1, 1)
        self.password_lab = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_lab.sizePolicy().hasHeightForWidth())
        self.password_lab.setSizePolicy(sizePolicy)
        self.password_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lab.setObjectName("password_lab")
        self.gridLayout.addWidget(self.password_lab, 1, 0, 1, 1)
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_input.sizePolicy().hasHeightForWidth())
        self.password_input.setSizePolicy(sizePolicy)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 1)
        self.login_BUT = QtWidgets.QPushButton(self.centralwidget)
        self.login_BUT.clicked.connect(self.__login_func)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_BUT.sizePolicy().hasHeightForWidth())
        self.login_BUT.setSizePolicy(sizePolicy)
        self.login_BUT.setObjectName("login_BUT")
        self.gridLayout.addWidget(self.login_BUT, 2, 0, 1, 1)
        self.error_lab = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_lab.sizePolicy().hasHeightForWidth())
        self.error_lab.setSizePolicy(sizePolicy)
        self.error_lab.setText("")
        self.error_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.error_lab.setObjectName("error_lab")
        self.error_lab.setStyleSheet("color : red")
        self.error_lab.hide()
        self.gridLayout.addWidget(self.error_lab, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("login", "login"))
        self.user_name_lab.setText(_translate("login", "الاسم"))
        self.password_lab.setText(_translate("login", "كلمه المرور"))
        self.login_BUT.setText(_translate("login", "تسجيل الدخول"))

    def __login_func(self):
        name = self.user_name_input.text()
        password = self.password_input.text()
        if name == "yaya9494" :
            if password == "8063" :
                self.MainWindow = mainWindow.MainWindow(True)
                self.MainWindow.show()
                self.hide()
            else:
                self.error_lab.setText("كلمه المرور خاطئه")
                self.error_lab.show()
        elif name == "12345":
            if password == "12345":
                self.MainWindow = mainWindow.MainWindow(False)
                self.MainWindow.show()
                self.hide()
            else:
                self.error_lab.setText("كلمه المرور خاطئه")
                self.error_lab.show()
        else:
            self.error_lab.setText("خطأ اسم المستخدم او كلمه المرور")
            self.error_lab.show()



