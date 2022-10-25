from PyQt6.QtWidgets import*
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

class plot_area_wid_22(QWidget):
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout.addWidget(self.toolbar)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)