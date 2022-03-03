import Serror
import sys
import uuid

from PyQt5 import QtWidgets

import login

if __name__ == "__main__" and hex(uuid.getnode()) == "0x8d0b7aaec4d5":
    app = QtWidgets.QApplication(sys.argv)
    loginPage = login.login()
    loginPage.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Serror.Ui_support_error()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
