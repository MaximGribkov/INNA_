import os
import sys

from PyQt6 import QtWidgets, QtGui
from gui_py.control_new import Ui_control
from gui_py.cooling_new import Ui_cooling
from gui_py.main_new import Ui_MainWindow
from gui_py.scheme_new import Ui_scheme


class ControlWindow(QtWidgets.QMainWindow, Ui_control):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.control = QtWidgets.QWidget()
        self.ui_control = Ui_control()
        self.ui_control.setupUi(self.control)
        self.control.setWindowIcon(QtGui.QIcon('img/control_icon.svg'))
        self.control.show()


class SchemeWindow(QtWidgets.QMainWindow, Ui_scheme):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scheme = QtWidgets.QDialog()
        self.ui_scheme = Ui_scheme()
        self.ui_scheme.setupUi(self.scheme)
        self.scheme.setWindowIcon(QtGui.QIcon('img/scheme_icon.svg'))
        self.scheme.show()


class CoolingWindow(QtWidgets.QMainWindow, Ui_cooling):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cooling = QtWidgets.QDialog()
        self.ui_cooling = Ui_cooling()
        self.ui_cooling.setupUi(self.cooling)
        self.cooling.setWindowIcon(QtGui.QIcon('img/cooling_icon.svg'))
        self.cooling.show()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main_window = Ui_MainWindow()
        self.ui_main_window.setupUi(self)


        # button connect
        self.ui_main_window.pushButton_close.clicked.connect(app.quit)
        self.ui_main_window.pushButton_open_control.clicked.connect(self.open_control)
        self.ui_main_window.pushButton_open_scheme.clicked.connect(self.open_scheme)
        self.ui_main_window.pushButton_open_cooling.clicked.connect(self.open_cooling)

    def open_control(self):
        if os.path.exists("time_data.txt"):
            os.remove("time_data.txt")
        ControlWindow(self)

    def open_scheme(self):
        SchemeWindow(self)

    def open_cooling(self):
        CoolingWindow(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon('img/main_icon.svg'))
    window.show()
    sys.exit(app.exec())
