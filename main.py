# import sys

# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# # Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")
#         button = QPushButton("Press Me!")

#         # Set the central widget of the Window.
#         self.setCentralWidget(button)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()


from test_gui import Ui_MainWindow

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow



class MyMainWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())