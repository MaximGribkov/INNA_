from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QPixmap, QPainter
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SVG Icon Example")
        self.setGeometry(100, 100, 400, 400)

        # Создаем виджет-контейнер для отображения SVG-иконки
        container_widget = QWidget()
        layout = QVBoxLayout()
        container_widget.setLayout(layout)

        # Загружаем SVG-файл и создаем QPixmap
        svg_renderer = QSvgRenderer("img/control_icon.svg")
        pixmap = QPixmap(300, 300)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        svg_renderer.render(painter)
        painter.end()

        # Создаем метку и устанавливаем в нее SVG-иконку
        self.icon_label = QLabel()
        self.icon_label.setPixmap(pixmap)
        layout.addWidget(self.icon_label)

        # Устанавливаем контейнер-виджет в качестве центрального виджета окна
        self.setCentralWidget(container_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())