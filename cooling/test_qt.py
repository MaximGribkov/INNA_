from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sys
from monitor import Ui_MainWindow
from modbusRTU import run_sync_client_temp, run_sync_client_flow


class Monitor(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Monitor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # ----------------------------------------
        self.ui.button_exit.clicked.connect(sys.exit)
        self.ui.button_on_drive.clicked.connect(self.on_off_drive)

        self.ui.label_temp.setText("{}".format(run_sync_client_temp()))
        self.ui.label_speed.setText("{}".format(run_sync_client_flow()))

    def on_off_drive(self):
        self.result = QMessageBox(self)

        self.result.setText("Включить или выключить привод ?")
        self.result.setWindowTitle("Монитор")
        self.result.setIcon(QMessageBox.Icon.Question)

        cansel = self.result.addButton('Отмена', self.result.ButtonRole.RejectRole)
        self.result.setDefaultButton(cansel)

        self.on = self.result.addButton('Включить', self.result.ButtonRole.AcceptRole)
        self.off = self.result.addButton('Выключить', self.result.ButtonRole.AcceptRole)

        self.result.buttonClicked.connect(self.answer_on_off_driver)
        self.result.exec()

    def answer_on_off_driver(self, e):
        # todo сделать проверку на работающий клапан
        if e.text() == "Включить":
            print('Включить')
            print(run_sync_client_temp())

        elif e.text() == "Выключить":
            print("Выключить")
            print(run_sync_client_flow())
            self.ui.label_temp.setStyleSheet("background-color:red")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Monitor()
    window.show()

    app.exec()
