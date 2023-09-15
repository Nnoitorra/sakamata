from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QPushButton, QVBoxLayout, QLabel, QStatusBar
from pathlib import Path
import functions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python tools")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(False)
        tabs.addTab(DlpTab(), "DLP")
        tabs.addTab(YtaTab(), "YTA")

        self.setCentralWidget(tabs)
        
class DlpTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.button = QPushButton("Run DLP")
        self.button.clicked.connect(self.button_clicked)

        self.label = QLabel()

        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def button_clicked(self):
        self.label.setText("Running DLP")
        functions.open_console()


class YtaTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.button = QPushButton("Run YTA")
        layout.addWidget(self.button)
        self.setLayout(layout)
        

app = QApplication([])
# app.setStyleSheet(Path(r"C:\Users\mueller\Documents\VSC\Python\PyQt\ui.qss").read_text())
window = MainWindow()
window.show()
app.exec()