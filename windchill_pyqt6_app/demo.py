import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QHBoxLayout,
    QLabel, QCheckBox, QComboBox, QLineEdit,
    QTextEdit, QWidget, QPushButton
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Create our Layouts
        main_layout = QVBoxLayout()

        # QLabel Example
        title_label = QLabel("Title for my App")

        # Set the font
        title_font = title_label.font()
        title_font.setPointSize(30)
        title_label.setFont(title_font)

        # Align the label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                 Qt.AlignmentFlag.AlignTop)

        # Add label to main_layout
        main_layout.addWidget(title_label)

        # Line Edit
        self.name_line = QLineEdit()
        self.name_line.setPlaceholderText("Name goes here")
        main_layout.addWidget(self.name_line)

        # Checkboxes
        self.this_checkbox = QCheckBox()
        this_label = QLabel("this")
        this_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.that_checkbox = QCheckBox()
        that_label = QLabel("that")
        that_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Add checkboxes to horizontal layouts
        check_box_row = QHBoxLayout()
        check_box_row.setAlignment(Qt.AlignmentFlag.AlignLeft |
                                   Qt.AlignmentFlag.AlignVCenter)
        check_box_row.addWidget(self.this_checkbox)
        check_box_row.addWidget(this_label)
        check_box_row.addWidget(self.that_checkbox)
        check_box_row.addWidget(that_label)

        # Add row to vertical layout
        main_layout.addLayout(check_box_row)

        # Combo boxes
        self.option_box = QComboBox()
        self.option_box.addItems(["Rancho Cucamonga, California",
                                  "Boring, Oregon", "Batman, Turkey",
                                  "Embarrass, Minnesota",
                                  "Toad Suck, Arkansas"])

        main_layout.addWidget(self.option_box)

        # Button to get all the things
        self.get_the_stuff_button = QPushButton("Get the stuff")
        self.get_the_stuff_button.clicked.connect(self.get_stuff)
        main_layout.addWidget(self.get_the_stuff_button)

        # Results window
        self.results_window = QTextEdit("Results")
        main_layout.addWidget(self.results_window)

        # Set the main Layout
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)

    def get_stuff(self):
        output = ""
        # Get all the stuff
        name = self.name_line.text()
        output += f"<p><b>Name</b>: {name}</p>"

        boxes_checked = "<p><b>Check Boxes that are checked</b>:</p><ul>"
        if self.this_checkbox.isChecked():
            boxes_checked += "<li>this</li>"
        if self.that_checkbox.isChecked():
            boxes_checked += "<li>that</li>"
        boxes_checked += "</ul>"
        output += boxes_checked

        # Get the combobox value
        city = self.option_box.currentText()
        output += f"<p><b>Combo Box selected</b> = {city}</p>"
        self.results_window.setText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
