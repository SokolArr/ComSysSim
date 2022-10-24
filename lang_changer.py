from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt6.uic import loadUi
from PyQt6 import QtGui

from helpers.replacer_lang import *

class MainFunc(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("./ui_components/lang_changer.ui",self)
        self.setWindowIcon(QtGui.QIcon('./pictures/icon.png'))
    
        self.btn_eng.clicked.connect(self.btn_eng_handler)
        self.btn_rus.clicked.connect(self.btn_rus_handler)
        
    def btn_eng_handler(self):
        change_to_ENG()
        self.result_label.setText("Done, language changed to English!")
        
    def btn_rus_handler(self):
        change_to_RUS()  
        self.result_label.setText("Готово, язык изменен на Русский!")  

app = QApplication([])
window = MainFunc()
window.show()
app.exec()