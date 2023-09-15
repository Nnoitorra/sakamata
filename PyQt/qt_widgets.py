from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        label = QLabel("Hello")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        # widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        checkbox = QCheckBox()
        checkbox.setCheckState(Qt.Checked)
        checkbox.stateChanged.connect(self.show_state)

        combobox = QComboBox()
        combobox.addItems(["One", "Two", "Three"])
        # current index of selected item
        combobox.currentIndexChanged.connect(self.index_changed)
        # send the text
        combobox.currentTextChanged.connect(self.text_changed)

        list = QListWidget()
        list.addItems(["One", "Two", "Three"])
        list.currentItemChanged.connect(self.index_changed_list)
        list.currentTextChanged.connect(self.text_changed)

        lineedit = QLineEdit()
        lineedit.setMaxLength(10)
        lineedit.setPlaceholderText("Enter your text")
        #lineedit.setReadOnly(True) # uncomment to make read-only
        lineedit.textChanged.connect(self.text_changed)
        lineedit.textEdited.connect(self.text_edited)

        spinbox = QSpinBox()
        spinbox.setMinimum(-10)
        spinbox.setMaximum(3)   # or spinbox.setRange(-10,3)
        spinbox.setPrefix("$")
        spinbox.setSuffix("c")
        spinbox.setSingleStep(3)
        spinbox.valueChanged.connect(self.value_changed)
        spinbox.textChanged.connect(self.text_changed)

        slider = QSlider()
        slider.setRange(-10,3)
        slider.setSingleStep(3)
        slider.valueChanged.connect(self.value_changed)
        slider.sliderMoved.connect(self.slider_position)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)

        dial = QDial()
        dial.setRange(-10,100)
        dial.setSingleStep(5)
        dial.valueChanged.connect(self.value_changed)
        dial.sliderMoved.connect(self.slider_position)
        dial.sliderPressed.connect(self.slider_pressed)
        dial.sliderReleased.connect(self.slider_released)

        layout.addWidget(label)
        layout.addWidget(checkbox)
        layout.addWidget(combobox)
        layout.addWidget(list)
        layout.addWidget(lineedit)
        layout.addWidget(spinbox)
        layout.addWidget(slider)
        layout.addWidget(dial)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)

    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s):  # s is a str
        print(s)

    def index_changed_list(self, i): # i is a QListWidgetItem
        print(i.text())

    def text_edited(self, s):
        print("Text edited...")
        print(s)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")

        

app = QApplication([])
window = MainWindow()
window.show()
app.exec()