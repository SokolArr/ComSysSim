from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt6.uic import loadUi

import numpy as np

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import plot_PSK as PSK
import plot_QAM as QAM


class MainFunc(QMainWindow):
    mes = []  
    
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("run2.ui",self)
        
        self.apply_PSK_but.stateChanged.connect(self.apply_PSK_but_handler)
        self.apply_QAM_but.stateChanged.connect(self.apply_QAM_but_handler)
        
        self.plot_QAM.clicked.connect(self.check_but_QAM) #Buttons
        self.plot_PSK.clicked.connect(self.check_but_PSK) #Buttons
        
        self.combobox_signal_type_QAM.currentTextChanged.connect(self.signal_QAM_handler)
        self.combobox_signal_type_PSK.currentTextChanged.connect(self.signal_PSK_handler)
        
        self.combobox_coef_QAM.currentTextChanged.connect(self.coef_QAM_handler)
        self.combobox_coef_PSK.currentTextChanged.connect(self.coef_PSK_handler)
        
        self.combobox_decision_QAM.setEnabled(False)
        self.combobox_decision_PSK.setEnabled(False)
        self.plot_QAM.setEnabled(False)
        self.plot_PSK.setEnabled(False)
        
        # self.addToolBar(NavigationToolbar(self.plot_constel_psk.canvas, self))
        self.addToolBar(NavigationToolbar(self.plot_area_wid.canvas, self))
        
        
    
    def apply_PSK_but_handler(self):
        if self.apply_PSK_but.isChecked() == True:
            self.plot_PSK.setEnabled(True)
        else:
            self.plot_PSK.setEnabled(False)
            
    def apply_QAM_but_handler(self):
        if self.apply_QAM_but.isChecked() == True:
            self.plot_QAM.setEnabled(True)
        else:
            self.plot_QAM.setEnabled(False)
        
    def check_but_QAM(self):
        if self.apply_QAM_but.isChecked() == True:
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
            
            msg_x = np.repeat(range(len(mes)), 2)
            msg_y = np.repeat(mes, 2)
            msg_x = msg_x[1:]
            msg_y = msg_y[:-1]
            msg_x = np.append(msg_x,msg_x[-1] + 1)
            msg_y = np.append(msg_y, msg_y[-1])
            
            mod, newMod, demod, modem1 = QAM.runEngineQAM(mes, int(M), int(noise_coef), grey_cod, bin_input, soft_decis, bin_output)
        
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
            
            temp = abs(np.subtract(mes,demod))
            # print(temp)
            
            if self.checkBox_show_sig_cons_qam.isChecked() == True:
                modem1.plot_const()            
            
            self.plot_area_wid.canvas.axes.clear()
            self.plot_area_wid.canvas.axes.plot(abs(np.subtract(mes,demod)))
            self.plot_area_wid.canvas.axes.set_title("Subtract original signal and demodulated signal")
            self.plot_area_wid.canvas.axes.set_xlabel('t, s')
            self.plot_area_wid.canvas.axes.set_ylabel('A, V')
            
            
            self.plot_area_wid.canvas.axes.grid()
            self.plot_area_wid.canvas.draw()

    def check_but_PSK(self):
        if self.apply_PSK_but.isChecked() == True:
            if self.combobox_signal_type_PSK.currentText() == 'Binary':
                bin_input = True
                bin_output = True
            if self.combobox_signal_type_PSK.currentText() == 'Integers':
                bin_input = False
                bin_output = False
                
            if self.combobox_decision_PSK.currentText() == 'Not soft':
                soft_decis = False
            if self.combobox_decision_PSK.currentText() == 'Soft':
                soft_decis = True
            if self.combobox_grey_PSK.currentText() == 'Yes':
                grey_cod = True
            if self.combobox_grey_PSK.currentText() == 'No':
                grey_cod = False
            inpText = self.PSK_input.text()
            mes = list(map(int, inpText))
            M = self.combobox_coef_PSK.currentText()
            noise_coef = self.combobox_noise_PSK.currentText()
            phase = self.combobox_phase_PSK.currentText()
            
            msg_x = np.repeat(range(len(mes)), 2)
            msg_y = np.repeat(mes, 2)
            msg_x = msg_x[1:]
            msg_y = msg_y[:-1]
            msg_x = np.append(msg_x,msg_x[-1] + 1)
            msg_y = np.append(msg_y, msg_y[-1])
            
            
            mod, newMod, demod, modem2= PSK.runEnginePSK(mes, int(M), int(noise_coef), int(phase), grey_cod, bin_input, soft_decis, bin_output)
        
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
            
                        
            temp = abs(np.subtract(mes,demod))
            # print(temp)
            
            if self.checkBox_show_sig_cons_psk.isChecked() == True:
                modem2.plot_const()
            
            # self.plot_constel_psk.canvas.axes.clear()
            # for i in range(1,1):
            #     self.plot_constel_psk.canvas.axes.plot(1, i, 'o', color='green') 
            # self.plot_constel_psk.canvas.axes.grid()
            # self.plot_constel_psk.canvas.draw()
            
            self.plot_area_wid.canvas.axes.clear()
            self.plot_area_wid.canvas.axes.plot(abs(np.subtract(mes,demod)))
            self.plot_area_wid.canvas.axes.set_title("Subtract original signal and demodulated signal")
            self.plot_area_wid.canvas.axes.set_xlabel('t, s')
            self.plot_area_wid.canvas.axes.set_ylabel('A, V')
            self.plot_area_wid.canvas.axes.grid()
            self.plot_area_wid.canvas.draw()

    def signal_QAM_handler(self):
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
                
    def signal_PSK_handler(self):
        if int(self.combobox_coef_PSK.currentText()) < 32:
            pow = int(self.combobox_coef_PSK.currentText())
            self.PSK_input.setMaxLength(2**(pow-1))      
            print(2**(pow-1))
        else:
            self.PSK_input.setMaxLength(32000)     
                
        if self.combobox_signal_type_PSK.currentText() == 'Binary':
                self.combobox_decision_PSK.setEnabled(True)
        if self.combobox_signal_type_PSK.currentText() == 'Integers':
                self.combobox_decision_PSK.setEnabled(False)
                self.PSK_input.setMaxLength(32000)
                
    def coef_QAM_handler(self):
        if self.combobox_signal_type_QAM.currentText() == 'Binary':
            if int(self.combobox_coef_QAM.currentText()) < 30:
                pow = int(self.combobox_coef_QAM.currentText())
                self.QAM_input.setMaxLength(2**(pow-1))      
                print(2**(pow-1))
        else:
                self.QAM_input.setMaxLength(32000)      
                
    def coef_PSK_handler(self):
        if self.combobox_signal_type_PSK.currentText() == 'Binary':
            if int(self.combobox_coef_PSK.currentText()) < 30:
                pow = int(self.combobox_coef_PSK.currentText())
                self.PSK_input.setMaxLength(2**(pow-1))      
                print(2**(pow-1))
        else:
                self.PSK_input.setMaxLength(32000)   
        
    def check_apply_but_PSK(self):
        print(self.apply_PSK_but.isChecked())

        
    def draw_graph(self):
        # plot_PSK.mainFunc()
        
        print(self.mes)
        
        self.plot_area_wid.canvas.axes.clear()
        self.plot_area_wid.canvas.axes.plot([1]) 
        
        self.plot_area_wid.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        self.plot_area_wid.canvas.axes.set_title('График')
        self.plot_area_wid.canvas.draw()
    


app = QApplication([])
window = MainFunc()
window.show()
app.exec()
