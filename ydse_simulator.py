import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QSlider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class YDSESimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Young\'s Double-Slit Experiment Simulator')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create a Matplotlib figure and a canvas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.create_widgets()
        self.show()

    def create_widgets(self):
        # Wavelength Slider
        self.wavelength_label = QLabel('Wavelength (nm): 500')
        self.wavelength_slider = QSlider()
        self.wavelength_slider.setOrientation(1)  # Horizontal
        self.wavelength_slider.setMinimum(100)  # Minimum wavelength in nm
        self.wavelength_slider.setMaximum(800)  # Maximum wavelength in nm
        self.wavelength_slider.setValue(500)  # Default value
        self.wavelength_slider.valueChanged.connect(self.update_label_and_plot)

        # Slit Separation Slider (in mm)
        self.slit_label = QLabel('Slit Separation (mm): 5.0')  # Default to 5.0 mm
        self.slit_slider = QSlider()
        self.slit_slider.setOrientation(1)  # Horizontal
        self.slit_slider.setMinimum(1)  # Minimum slit separation in mm
        self.slit_slider.setMaximum(100)  # Maximum slit separation in mm
        self.slit_slider.setValue(5)  # Default value (5 mm)
        self.slit_slider.valueChanged.connect(self.update_label_and_plot)

        # Adding widgets to the layout
        self.layout.addWidget(self.wavelength_label)
        self.layout.addWidget(self.wavelength_slider)
        self.layout.addWidget(self.slit_label)
        self.layout.addWidget(self.slit_slider)

        # Initial plot
        self.update_label_and_plot()

    def update_label_and_plot(self):
        self.wavelength_label.setText(f'Wavelength (nm): {self.wavelength_slider.value()}')
        self.slit_label.setText(f'Slit Separation (mm): {self.slit_slider.value()}')  # Value in mm
        
        # Update the interference pattern in real-time
        self.visualize_pattern()

    def visualize_pattern(self):
        # Get current values
        wavelength = self.wavelength_slider.value() * 1e-9  # Convert nm to meters
        slit_separation = self.slit_slider.value() * 1e-3  # Convert mm to meters
        
        # Create a new figure for the interference pattern
        self.figure.clear()  # Clear previous plots
        ax = self.figure.add_subplot(111)  # Add subplot

        screen_distance = 1.0  # Distance from slits to screen (in meters)
        num_points = 1000  # Number of points to sample on the screen
        x = np.linspace(-0.5, 0.5, num_points)  # Screen position
        intensity = (np.sin(np.pi * slit_separation * x / (wavelength * screen_distance)))**2

        ax.plot(x, intensity, color='blue')
        ax.set_title('Interference Pattern')
        ax.set_xlabel('Position on Screen (m)')
        ax.set_ylabel('Intensity (arbitrary units)')
        ax.set_ylim(0, 1)
        ax.grid()

        self.canvas.draw()  # Update the plot on the canvas

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YDSESimulator()
    sys.exit(app.exec_())
