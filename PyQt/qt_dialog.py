from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        # dlg = QMessageBox(self)
        # dlg.setWindowTitle("I have a question!")
        # dlg.setText("This is a simple dialog")
        # dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # dlg.setIcon(QMessageBox.Question)
        # button = dlg.exec()

        # button = QMessageBox.question(self, "Question dialog", "The longer message")

        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard
        )
        
        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print()

class CustomDialog(QDialog): # call with dlg = CustomDialog(self)
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()