import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QHBoxLayout,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QWidget,
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

        # Checkboxes
        this_checkbox = QCheckBox()
        this_label = QLabel("this")
        this_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        that_checkbox = QCheckBox()
        that_label = QLabel("that")
        that_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Add checkboxes to horizontal layouts
        check_box_row = QHBoxLayout()
        check_box_row.setAlignment(Qt.AlignmentFlag.AlignLeft |
                                   Qt.AlignmentFlag.AlignVCenter)
        check_box_row.addWidget(this_checkbox)
        check_box_row.addWidget(this_label)
        check_box_row.addWidget(that_checkbox)
        check_box_row.addWidget(that_label)

        # Add row to vertical layout
        main_layout.addLayout(check_box_row)

        # Set the main Layout
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()