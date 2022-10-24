from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt6.uic import loadUi
from PyQt6 import QtGui


import numpy as np
import random

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import modulations.engine_PSK as PSK
import modulations.engine_QAM as QAM

from helpers.msg_to_bin import msg_to_bin
from helpers.plots_draw.draw_11 import draw_11
from helpers.plots_draw.draw_12 import draw_12
from helpers.plots_draw.draw_13 import draw_13
from helpers.plots_draw.draw_14 import draw_14
from helpers.plots_draw.draw_2 import draw_2

class MainFunc(QMainWindow):
    mes = []
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("./ui_components/actual_lang.ui",self)
        self.setWindowIcon(QtGui.QIcon('./pictures/icon.png'))
        
        self.apply_PSK_but.stateChanged.connect(self.apply_PSK_but_handler)
        self.apply_QAM_but.stateChanged.connect(self.apply_QAM_but_handler)
        
        self.PSK_input.textChanged.connect(self.PSK_input_change_handler)
        self.length_PSK_mes.setText(str(self.PSK_input.text().__len__()))
        
        self.QAM_input.textChanged.connect(self.QAM_input_change_handler)
        self.length_QAM_mes.setText(str(self.QAM_input.text().__len__()))
        
        self.plot_QAM.clicked.connect(self.check_but_QAM) #Buttons
        self.plot_PSK.clicked.connect(self.check_but_PSK) #Buttons
        
        self.pushButton_generate_sid_PSK.clicked.connect(self.generate_sid_PSK_handler) #Buttons
        self.pushButton_generate_sid_QAM.clicked.connect(self.generate_sid_QAM_handler) #Buttons
        
        self.combobox_signal_type_QAM.currentTextChanged.connect(self.signal_QAM_handler)
        self.combobox_signal_type_PSK.currentTextChanged.connect(self.signal_PSK_handler)
        
        self.combobox_coef_QAM.currentTextChanged.connect(self.coef_QAM_handler)
        self.combobox_coef_PSK.currentTextChanged.connect(self.coef_PSK_handler)
        
        self.combobox_decision_QAM.setEnabled(False)
        self.combobox_decision_PSK.setEnabled(False)
        
        self.plot_QAM.setEnabled(False)
        self.plot_PSK.setEnabled(False)
        
        self.progressBar_PSK.setValue(0)
        self.progressBar_QAM.setValue(0)
        
        # self.addToolBar(NavigationToolbar(self.plot_constel_psk.canvas, self))
        # self.addToolBar(NavigationToolbar(self.plot_area_wid.canvas, self))
        
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
            
            
    def generate_sid_PSK_handler(self):
        self.progressBar_PSK.setValue(0)
        n_max = 1
        if self.all_numbers_PSK.isChecked() == False:
            n_max = int(self.combobox_coef_PSK.currentText()) - 1 
        rand_list=[]
        
        n = int(self.spinBox_PSK.value() )
        
        self.progressBar_PSK.setValue(50)
        
        for i in range(n):
            rand_list.append(random.randint(0,n_max))
        self.progressBar_PSK.setValue(70)
        
        self.plainText_sid_PSK.setPlainText(' '.join(str(x) for x in rand_list))
        
        self.progressBar_PSK.setValue(100)
        
    def generate_sid_QAM_handler(self):
        self.progressBar_QAM.setValue(0)
        n_max = 1
        if self.all_numbers_QAM.isChecked() == False:
            n_max = int(self.combobox_coef_QAM.currentText()) - 1 
        rand_list=[]
        n = int(self.spinBox_QAM.value() )
        self.progressBar_QAM.setValue(50)
        for i in range(n):
            rand_list.append(random.randint(0,n_max))
        self.progressBar_QAM.setValue(70)
        self.plainText_sid_QAM.setPlainText(' '.join(str(x) for x in rand_list))
        self.progressBar_QAM.setValue(100)


    def check_but_QAM(self):
        if self.apply_QAM_but.isChecked() == True:
            self.progressBar_QAM.setValue(0)
            is_it_latters = False
            bin_input, bin_output, is_it_latters = check_combobox_QAM(self)
 
            if self.combobox_decision_QAM.currentText() == 'Not soft':
                soft_decis = False
            if self.combobox_decision_QAM.currentText() == 'Soft':
                soft_decis = True
            if self.combobox_grey_QAM.currentText() == 'Yes':
                grey_cod = True
            if self.combobox_grey_QAM.currentText() == 'No':
                grey_cod = False
                
            if is_it_latters == False:    
                inpText = self.QAM_input.text()
                mes = [int(s) for s in inpText.split() if s.isdigit()]
                
            if is_it_latters == True:  
                inpText = msg_to_bin(self.QAM_input.text())
                mes = [int(s) for s in inpText.split() if s.isdigit()]
            
            M = self.combobox_coef_QAM.currentText()
            noise_coef = self.combobox_noise_QAM.currentText()
            
            msg_x = np.repeat(range(len(mes)), 2)
            msg_y = np.repeat(mes, 2)
            msg_x = msg_x[1:]
            msg_y = msg_y[:-1]
            msg_x = np.append(msg_x,msg_x[-1] + 1)
            msg_y = np.append(msg_y, msg_y[-1])
            
            mod, newMod, demod, modem1 = QAM.runEngineQAM(mes, int(M), int(noise_coef), grey_cod, bin_input, soft_decis, bin_output)
        
            self.progressBar_QAM.setValue(50)    
            
            ch = 0
            for index in range(mes.__len__()):
                if mes[index] != demod[index]:
                    ch = ch + 1
                    
            dmessage_length = demod.__len__()
            if dmessage_length < 10000:
                self.dmessage_template.setText(str(demod))
            else:
                self.dmessage_template.setText("Big message!")
            
            self.label_bit_error.setText("Bit errors: " + str(ch))
            
            self.message_template.setText(str(mes))
            self.type_mod.setText("Type modulation: QAM")
    
            
            self.progressBar_QAM.setValue(60)
            
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
            
            if self.checkBox_show_sig_cons_qam.isChecked() == True:
                modem1.plot_const()            
            
            self.progressBar_QAM.setValue(50)

            draw_2(self, mes, demod)
            draw_11(self, msg_x, msg_y, "QAM")
            self.progressBar_QAM.setValue(75)
            draw_12(self, mod_reals, mod_imags, "QAM")
            self.progressBar_QAM.setValue(80)
            draw_13(self, dmsg_x, dmsg_y, "QAM")
            self.progressBar_QAM.setValue(90)
            draw_14(self, n_mod_reals, n_mod_imags, "QAM")
            
            self.progressBar_QAM.setValue(100)

    def check_but_PSK(self):
        if self.apply_PSK_but.isChecked() == True:
            self.progressBar_PSK.setValue(0)

            is_it_latters = False
            bin_input, bin_output, is_it_latters = check_combobox_PSK(self)
        
            if self.combobox_decision_PSK.currentText() == 'Not soft':
                soft_decis = False
            if self.combobox_decision_PSK.currentText() == 'Soft':
                soft_decis = True
            if self.combobox_grey_PSK.currentText() == 'Yes':
                grey_cod = True
            if self.combobox_grey_PSK.currentText() == 'No':
                grey_cod = False
            
            if is_it_latters == False:    
                inpText = self.PSK_input.text()
                mes = [int(s) for s in inpText.split() if s.isdigit()]
                
            if is_it_latters == True:  
                inpText = msg_to_bin(self.PSK_input.text())
                mes = [int(s) for s in inpText.split() if s.isdigit()]

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
            
            self.progressBar_PSK.setValue(50)    
                    
            ch = 0
            for index in range(mes.__len__()):
                if mes[index] != demod[index]:
                    ch = ch + 1
                    
                    
            dmessage_length = demod.__len__()
            if dmessage_length < 10000:
                self.dmessage_template.setText(str(demod))
            else:
                self.dmessage_template.setText("Big message!")
            
            self.label_bit_error.setText("Bit errors: " + str(ch))
            
            self.message_template.setText(str(mes))
            self.type_mod.setText("Type modulation: PSK")
    
            self.progressBar_PSK.setValue(60)
            
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
            
            if self.checkBox_show_sig_cons_psk.isChecked() == True:
                modem2.plot_const()
            
            self.progressBar_PSK.setValue(50)
            
            draw_2(self, mes, demod)
            draw_11(self, msg_x, msg_y, "PSK")
            self.progressBar_PSK.setValue(75)
            draw_12(self, mod_reals, mod_imags, "PSK")
            self.progressBar_PSK.setValue(80)
            draw_13(self, dmsg_x, dmsg_y, "PSK")
            self.progressBar_PSK.setValue(90)
            draw_14(self, n_mod_reals, n_mod_imags, "PSK")
            
            self.progressBar_PSK.setValue(100)
            
            
    def signal_QAM_handler(self):
        if int(self.combobox_coef_QAM.currentText()) < 32:
            pow = int(self.combobox_coef_QAM.currentText())
            self.QAM_input.setMaxLength(2**(pow-1)* 2)      
        else:
            self.QAM_input.setMaxLength(32000)     
                
        if self.combobox_signal_type_QAM.currentText() == 'Binary code':
                self.combobox_decision_QAM.setEnabled(True)
        if self.combobox_signal_type_QAM.currentText() == 'Only integers':
                self.combobox_decision_QAM.setEnabled(False)
                self.QAM_input.setMaxLength(32000)
                
    def signal_PSK_handler(self):
        if int(self.combobox_coef_PSK.currentText()) < 32:
            pow = int(self.combobox_coef_PSK.currentText())
            self.PSK_input.setMaxLength(2**(pow-1) * 2)      
        else:
            self.PSK_input.setMaxLength(32000)     
                
        if self.combobox_signal_type_PSK.currentText() == 'Binary code':
                self.combobox_decision_PSK.setEnabled(True)
        if self.combobox_signal_type_PSK.currentText() == 'Only integers':
                self.combobox_decision_PSK.setEnabled(False)
                self.PSK_input.setMaxLength(32000)
               
                
    def coef_QAM_handler(self):
        if self.combobox_signal_type_QAM.currentText() == 'Binary code':
            if int(self.combobox_coef_QAM.currentText()) < 30:
                pow = int(self.combobox_coef_QAM.currentText())
                self.QAM_input.setMaxLength(2**(pow-1)* 2)      
        else:
                self.QAM_input.setMaxLength(32000)      
                
    def coef_PSK_handler(self):
        if self.combobox_signal_type_PSK.currentText() == 'Binary code':
            if int(self.combobox_coef_PSK.currentText()) < 30:
                pow = int(self.combobox_coef_PSK.currentText())
                self.PSK_input.setMaxLength(2**(pow-1)* 2)      
        else:
                self.PSK_input.setMaxLength(32000)   

    def PSK_input_change_handler(self):
        self.length_PSK_mes.setText(str(self.PSK_input.text().__len__()))
        
    def QAM_input_change_handler(self):
        self.length_QAM_mes.setText(str(self.QAM_input.text().__len__()))
    



def check_combobox_QAM(self):
    bin_input = False
    bin_output = False
    is_it_letters = False
    if self.combobox_signal_type_QAM.currentText() == 'Binary code':
        bin_input = True
        bin_output = True
    if self.combobox_signal_type_QAM.currentText() == 'Only integers':
        bin_input = False
        bin_output = False
    if self.combobox_signal_type_QAM.currentText() == 'Message with letters':
        bin_input = True
        bin_output = True
        is_it_letters = True        
    return bin_input, bin_output, is_it_letters

def check_combobox_PSK(self):
    bin_input = False
    bin_output = False
    is_it_letters = False
    if self.combobox_signal_type_PSK.currentText() == 'Binary code':
        bin_input = True
        bin_output = True
    if self.combobox_signal_type_PSK.currentText() == 'Only integers':
        bin_input = False
        bin_output = False
    if self.combobox_signal_type_PSK.currentText() == 'Message with letters':
        bin_input = True
        bin_output = True
        is_it_letters = True  
    return bin_input, bin_output, is_it_letters



app = QApplication([])
window = MainFunc()
window.show()
app.exec()
