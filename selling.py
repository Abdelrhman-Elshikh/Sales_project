from PyQt5 import QtWidgets

import login
import mainWindow, uuid, Serror, sys

def save_DB():
    mainWindow.db.commit()

if __name__ == "__main__" and hex(uuid.getnode()) == "0xdb23200d686":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    app.lastWindowClosed.connect(lambda : save_DB)
    MainWindow = QtWidgets.QMainWindow()
    ui = login.Ui_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Serror.Ui_support_error()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
