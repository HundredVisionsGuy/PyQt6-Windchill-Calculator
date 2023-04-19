import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QHBoxLayout,
    QLabel, QCheckBox, QComboBox, QListWidget, QTextEdit,
    QSpinBox, QDoubleSpinBox, QSlider, QWidget, QPushButton,
)
from PyQt6.QtCore import Qt
import controller

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Windchill Calculator App")

        # Create our Layouts
        main_layout = QHBoxLayout()

        # Create 2 columns (each a VHBox)
        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()

        # Title label
        title_label = QLabel("Wind Chill Calculator")

        # Set the font
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)

        ############################
        # Widgets for the left pane
        ############################
        # Temperature inputs
        temperature_label = QLabel("Temperature:")
        self.temperature_spinbox = QSpinBox()
        self.temperature_spinbox.setMinimum(-100)
        self.temperature_spinbox.setMaximum(40)

        # Wind Speed inputs
        wind_label = QLabel("Wind Speed:")
        self.wind_spinbox = QSpinBox()
        self.wind_spinbox.setMinimum(0)
        self.wind_spinbox.setMaximum(40)

        # Results Pane Widgets
        results_title = QLabel("Results")
        results_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)
        h2_font = results_title.font()
        h2_font.setPointSize(26)
        results_title.setFont(h2_font)
        self.results_window = QTextEdit("Add instructions here")
        self.results_window.setMinimumHeight(100)
        
        self.calculate_button = QPushButton("Get Windspeed")
        # add a calculate function
        self.calculate_button.clicked.connect(self.calculate_windchill)

        # Align the label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)

        # Add our left pane widgets
        left_pane.addWidget(title_label)
        left_pane.addWidget(temperature_label)
        left_pane.addWidget(self.temperature_spinbox)
        left_pane.addWidget(wind_label)
        left_pane.addWidget(self.wind_spinbox)
        left_pane.addWidget(self.calculate_button)

        # Add our right pane widgets
        right_pane.addWidget(results_title)
        right_pane.addWidget(self.results_window)
        
        # Add the two panes to the layout
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)

        # Set the main Layout
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)
    
    def calculate_windchill(self):
        """Calculate windchill"""
        # Get temp
        temperature = self.temperature_spinbox.value()
        

        # Get windspeed
        windspeed = self.wind_spinbox.value()
        
        # Get windchill
        results = controller.get_windchill(temperature, windspeed)
        # Display results
        self.results_window.setText(results)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()