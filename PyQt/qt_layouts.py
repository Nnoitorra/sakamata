from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QTabWidget, QPushButton
from PyQt5.QtGui import QPalette, QColor


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # layout1 = QHBoxLayout()
        # layout2 = QVBoxLayout()
        # layout3 = QVBoxLayout()
        # layout2.addWidget(Color('red'))
        # layout2.addWidget(Color('yellow'))
        # layout2.addWidget(Color('purple'))
        # layout1.addLayout(layout2)
        # layout1.addWidget(Color('green'))
        # layout3.addWidget(Color('red'))
        # layout3.addWidget(Color('purple'))
        # layout1.addLayout(layout3)
        # layout1.setContentsMargins(0,0,0,0)
        # layout1.setSpacing(20)

        # layout = QGridLayout()
        # layout.addWidget(Color('red'), 0, 0)
        # layout.addWidget(Color('green'), 1, 0)
        # layout.addWidget(Color('blue'), 1, 1)
        # layout.addWidget(Color('purple'), 2, 1)

        # layout = QStackedLayout()
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('yellow'))
        # layout.setCurrentIndex(3)
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()