from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar
)

import plot_PSK as PSK
     
class MatplotlibWidget(QMainWindow):
    mes = []
    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("run2.ui",self)
        
        
        # self.apply_QAM_but.stateChanged.connect(self.check_apply_but_QAM)
        self.apply_PSK_but.stateChanged.connect(self.check_apply_but_PSK)
        self.plot_QAM.clicked.connect(self.check_but_QAM)
        
        self.combobox_signal_type_QAM.currentTextChanged.connect(self.signal_handler)
        self.combobox_coef_QAM.currentTextChanged.connect(self.coef_handler)
        self.combobox_decision_QAM.setEnabled(False)
        
        
        self.addToolBar(NavigationToolbar(self.plot_area_wid.canvas, self))

    def check_but_QAM(self):
        if self.apply_QAM_but.isChecked() == True:
            self.apply_PSK_but.setChecked(False)
            if self.combobox_signal_type_QAM.currentText() == 'Binary':
               bin_input = True
               bin_output = True
            if self.combobox_signal_type_QAM.currentText() == 'Integers':
               bin_input = False
               bin_output = False
               
            if self.combobox_decision_QAM.currentText() == 'Not soft':
                soft_decis = False
            if self.combobox_decision_QAM.currentText() == 'Soft':
                soft_decis = True
            if self.combobox_grey_QAM.currentText() == 'Yes':
                grey_cod = True
            if self.combobox_grey_QAM.currentText() == 'No':
                grey_cod = False
            inpText = self.QAM_input.text()
            mes = list(map(int, inpText))
            M = self.combobox_coef_QAM.currentText()
            noise_coef = self.combobox_noise_QAM.currentText()
            phase = self.combobox_phase_QAM.currentText()
            
            msg_x = np.repeat(range(len(mes)), 2)
            msg_y = np.repeat(mes, 2)
            msg_x = msg_x[1:]
            msg_y = msg_y[:-1]
            msg_x = np.append(msg_x,msg_x[-1] + 1)
            msg_y = np.append(msg_y, msg_y[-1])
            
            
            mod, newMod, demod = PSK.runEngine(mes, int(M), int(noise_coef), int(phase), grey_cod, bin_input, soft_decis, bin_output)
        
            dmsg = demod
            dmsg_x = np.repeat(range(len(dmsg)), 2)
            dmsg_y = np.repeat(dmsg, 2)
            dmsg_x = dmsg_x[1:]
            dmsg_y = dmsg_y[:-1]
            dmsg_x = np.append(dmsg_x,dmsg_x[-1] + 1)
            dmsg_y = np.append(dmsg_y, dmsg_y[-1])
            
            mod_reals = [ele.real for ele in mod]
            n_mod_reals = [ele.real for ele in newMod]
            # extract imaginary part
            mod_imags = [ele.imag for ele in mod]
            n_mod_imags = [ele.imag for ele in newMod]
            
            
            self.plot_area_wid.canvas.axes.clear()
            self.plot_area_wid.canvas.axes.plot(msg_x, msg_y, dmsg_x, dmsg_y)
            self.plot_area_wid.canvas.axes.grid()
            self.plot_area_wid.canvas.draw()
    
    def signal_handler(self):
        if int(self.combobox_coef_QAM.currentText()) < 32:
            pow = int(self.combobox_coef_QAM.currentText())
            self.QAM_input.setMaxLength(2**(pow-1))      
            print(2**(pow-1))
        else:
            self.QAM_input.setMaxLength(32000)     
             
        if self.combobox_signal_type_QAM.currentText() == 'Binary':
               self.combobox_decision_QAM.setEnabled(True)
        if self.combobox_signal_type_QAM.currentText() == 'Integers':
               self.combobox_decision_QAM.setEnabled(False)
               self.QAM_input.setMaxLength(32000)
               
    def coef_handler(self):
        if self.combobox_signal_type_QAM.currentText() == 'Binary':
            if int(self.combobox_coef_QAM.currentText()) < 30:
                pow = int(self.combobox_coef_QAM.currentText())
                self.QAM_input.setMaxLength(2**(pow-1))      
                print(2**(pow-1))
        else:
             self.QAM_input.setMaxLength(32000)      
        
    def check_apply_but_PSK(self):
        # print(self.apply_PSK_but.isChecked())
        PSK.runEngine()
        if self.apply_PSK_but.isChecked() == True:
            self.apply_QAM_but.setChecked(False)
            PSK.runEngine()
        
    def draw_graph(self):
        # plot_PSK.mainFunc()
        
        print(self.mes)
        
        self.plot_area_wid.canvas.axes.clear()
        self.plot_area_wid.canvas.axes.plot([1]) 
        
        # self.plot_area_wid.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        self.plot_area_wid.canvas.axes.set_title('График')
        self.plot_area_wid.canvas.draw()
        

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()