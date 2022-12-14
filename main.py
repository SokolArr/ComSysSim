#Импорт компонентов графической библиотеки
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from PyQt6 import QtGui

#Импорт библиотеки работы с данными
import numpy as np
import random
import string

#Импорт файлов с модуляциями
import modulations.engine_PSK as PSK
import modulations.engine_QAM as QAM

#Импорт файлов с модуляциями
from helpers.get_SIGMA import get_SIGMA
from helpers.msg_to_bin import msg_to_bin
from helpers.bin_to_msg import bin_to_msg
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
        
        #Инициализация элементов взаимодействия с интерфейсом
        self.apply_PSK_but.stateChanged.connect(self.apply_PSK_but_handler)
        self.apply_QAM_but.stateChanged.connect(self.apply_QAM_but_handler)
        
        self.PSK_input.textChanged.connect(self.PSK_input_change_handler)
        self.length_PSK_mes.setText(str(self.PSK_input.text().__len__()))
        
        self.QAM_input.textChanged.connect(self.QAM_input_change_handler)
        self.length_QAM_mes.setText(str(self.QAM_input.text().__len__()))
        
        self.plot_QAM.clicked.connect(self.check_but_QAM) 
        self.plot_PSK.clicked.connect(self.check_but_PSK) 
        
        self.pushButton_generate_sid_PSK.clicked.connect(self.generate_sid_PSK_handler) 
        self.pushButton_generate_sid_QAM.clicked.connect(self.generate_sid_QAM_handler)
        
        self.combobox_signal_type_QAM.currentTextChanged.connect(self.signal_QAM_handler)
        self.combobox_signal_type_PSK.currentTextChanged.connect(self.signal_PSK_handler)
        
        self.combobox_coef_QAM.currentTextChanged.connect(self.coef_QAM_handler)
        self.combobox_coef_PSK.currentTextChanged.connect(self.coef_PSK_handler)
        
        self.combobox_decision_QAM.setEnabled(False)
        self.combobox_decision_PSK.setEnabled(False)
        
        self.combobox_grey_QAM.setEnabled(False)
        self.combobox_grey_PSK.setEnabled(False)
        
        self.plot_QAM.setEnabled(False)
        self.plot_PSK.setEnabled(False)
        
        self.progressBar_PSK.setValue(0)
        self.progressBar_QAM.setValue(0)
    
    #Обработчик чекбокса применения настроек    
    def apply_PSK_but_handler(self):
        if self.apply_PSK_but.isChecked() == True:
            self.plot_PSK.setEnabled(True)
        else:
            self.plot_PSK.setEnabled(False)
            
    #Обработчик чекбокса применения настроек         
    def apply_QAM_but_handler(self):
        if self.apply_QAM_but.isChecked() == True:
            self.plot_QAM.setEnabled(True)
        else:
            self.plot_QAM.setEnabled(False)
            
    #Обработчик кнопки генерации случайного сообщения       
    def generate_sid_PSK_handler(self):
        n = int(self.spinBox_PSK.value() )
        rand_list=[]
        if self.all_numbers_PSK.isChecked() == True:
            for i in range(n):
                rand_list.append(random.randint(0, 1))
            self.plainText_sid_PSK.setPlainText(' '.join(str(x) for x in rand_list))
            
        if self.all_numbers_PSK.isChecked() == False:
            letters = string.ascii_lowercase
            self.plainText_sid_PSK.setPlainText(''.join(random.choice(letters) for i in range(n)))   
     
    #Обработчик кнопки генерации случайного сообщения   
    def generate_sid_QAM_handler(self):
        n = int(self.spinBox_QAM.value() )
        rand_list=[]
        if self.all_numbers_QAM.isChecked() == True:
            for i in range(n):
                rand_list.append(random.randint(0, 1))
            self.plainText_sid_QAM.setPlainText(' '.join(str(x) for x in rand_list))
            
        if self.all_numbers_QAM.isChecked() == False:
            letters = string.ascii_lowercase
            self.plainText_sid_QAM.setPlainText(''.join(random.choice(letters) for i in range(n)))

    #Обработчик кнопки генерации QAM модуляции
    def check_but_QAM(self):
        if self.apply_QAM_but.isChecked() == True:
            self.progressBar_QAM.setValue(0) #Установка прогресс бара в 0 процентов
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
                inpText = msg_to_bin(self.QAM_input.text()) #Обработчик настроек типа сообщения
                mes = [int(s) for s in inpText.split() if s.isdigit()]
            
            M = self.combobox_coef_QAM.currentText()
            
            mu = 0
            snr = self.inp_SNR_QAM.text()
            
            #Настройки для отрисовки графиков сигналов
            msg_x = np.repeat(range(len(mes)), 2)
            msg_y = np.repeat(mes, 2)
            msg_x = msg_x[1:]
            msg_y = msg_y[:-1]
            msg_x = np.append(msg_x,msg_x[-1] + 1)
            msg_y = np.append(msg_y, msg_y[-1])

            sigma_QAM = get_SIGMA("QAM", int(M), float(snr))
            
            #Запуск процесса модуляции и демодуляции
            mod, newMod, demod, modem1 = QAM.runEngineQAM(mes, int(M), float(mu), float(sigma_QAM), grey_cod, bin_input, soft_decis, bin_output)
            
            self.progressBar_QAM.setValue(50)
               
            #Формирование отчета модуляции
            ch = 0
            for index in range(mes.__len__()):
                if mes[index] != demod[index]:
                    ch = ch + 1
            
            arr_tmp_2 = []
            for el in demod:
                arr_tmp_2.append(int(el))   
            
            if self.combobox_signal_type_QAM.currentText() == 'Message with letters':
                arr_tmp = []
                for el in demod:
                    arr_tmp.append(str(int(el)))  
                demod_str = ''.join(arr_tmp)

                tmp = [demod_str[i:i+8] for i in range(0, len(demod_str), 8)]
                new_array = []
                for el in tmp:
                    new_array.append('0' + el[1:])
                    
                edit_mod_msg = ''.join(new_array)
                decoded_msg = bin_to_msg(edit_mod_msg)
                
                print ('Decoded msg:' + decoded_msg)
                
                self.tmtr_msg_bow.setText('Тип модуляции: ' + M + '-QAM' + '\n' + 'Отправленное сообщение: ' + 
                                          str(self.QAM_input.text()) +
                                          '\n' + '\n' + 'Битовое представление: ' + '\n' + str(mes))
                self.reisiv_msg_bow.setText('Декодированное сообщение: '+ 
                                          str(decoded_msg) + 
                                          '\n' + '\n' + 'Битовое представление: ' + '\n' + str(arr_tmp_2))
            else:
                self.tmtr_msg_bow.setText('Тип модуляции: ' + M + '-QAM' + '\n' +
                                          'Битовое представление: ' + '\n' + str(mes))
                self.reisiv_msg_bow.setText('Битовое представление: ' + '\n' + str(arr_tmp_2))
                                 
            self.textBrowse_BER.setText("Ошибочных битов: " + str(ch) +
                                         "\nВсего битов: " + str(demod.__len__()) +
                                         "\nBER: " + str(float(ch)/float(demod.__len__()))
                                         )                 
            
            self.progressBar_QAM.setValue(60)
            
            #Настройки для отрисовки графиков сигналов
            dmsg = demod
            dmsg_x = np.repeat(range(len(dmsg)), 2)
            dmsg_y = np.repeat(dmsg, 2)
            dmsg_x = dmsg_x[1:]
            dmsg_y = dmsg_y[:-1]
            dmsg_x = np.append(dmsg_x,dmsg_x[-1] + 1)
            dmsg_y = np.append(dmsg_y, dmsg_y[-1])
            
            mod_reals = [ele.real for ele in mod]
            n_mod_reals = [ele.real for ele in newMod]
            mod_imags = [ele.imag for ele in mod]
            n_mod_imags = [ele.imag for ele in newMod]
            
            if self.checkBox_show_sig_cons_qam.isChecked() == True:
                modem1.plot_const()            
            
            self.progressBar_QAM.setValue(50)

            #Функции вызова отрисовки графиков
            draw_2(self, mes, demod)
            draw_11(self, msg_x, msg_y, "QAM")
            self.progressBar_QAM.setValue(75)
            draw_12(self, mod_reals, mod_imags, "QAM")
            self.progressBar_QAM.setValue(80)
            draw_13(self, dmsg_x, dmsg_y, "QAM")
            self.progressBar_QAM.setValue(90)
            draw_14(self, n_mod_reals, n_mod_imags, "QAM")
            
            self.progressBar_QAM.setValue(100)

    #Обработчик кнопки генерации PSK модуляции
    def check_but_PSK(self):
        if self.apply_PSK_but.isChecked() == True:
            self.progressBar_PSK.setValue(0) #Установка прогресс бара в 0 процентов
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
                inpText = msg_to_bin(self.PSK_input.text()) #Обработчик настроек типа сообщения
                mes = [int(s) for s in inpText.split() if s.isdigit()]

            M = self.combobox_coef_PSK.currentText()
            
            mu = 0
            snr = self.inp_SNR_PSK.text()
            
            phase = self.combobox_phase_PSK.currentText()
            
            #Настройки для отрисовки графиков сигналов
            msg_x = np.repeat(range(len(mes)), 2)
            msg_y = np.repeat(mes, 2)
            msg_x = msg_x[1:]
            msg_y = msg_y[:-1]
            msg_x = np.append(msg_x,msg_x[-1] + 1)
            msg_y = np.append(msg_y, msg_y[-1])
            
            sigma_QAM = get_SIGMA("PSK", int(M), float(snr))
            
            #Запуск процесса модуляции и демодуляции
            mod, newMod, demod, modem2= PSK.runEnginePSK(mes, int(M), float(mu), float(sigma_QAM), int(phase), grey_cod, bin_input, soft_decis, bin_output)
            
            self.progressBar_PSK.setValue(50)    
            
            #Формирование отчета модуляции        
            ch = 0
            for index in range(mes.__len__()):
                if mes[index] != demod[index]:
                    ch = ch + 1
            
            arr_tmp_2 = []
            for el in demod:
                arr_tmp_2.append(int(el))
               
            if self.combobox_signal_type_PSK.currentText() == 'Message with letters':     
                arr_tmp = []
                for el in demod:
                    arr_tmp.append(str(int(el)))  
                demod_str = ''.join(arr_tmp)
                
                tmp = [demod_str[i:i+8] for i in range(0, len(demod_str), 8)]
                new_array = []
                for el in tmp:
                    new_array.append('0' + el[1:])
                edit_mod_msg = ''.join(new_array)
                decoded_msg = bin_to_msg(edit_mod_msg)
                
                print ('Decoded msg:' + decoded_msg)
                
                self.tmtr_msg_bow.setText('Тип модуляции: ' + M + '-PSK' + '\n' + 'Отправленное сообщение: ' + 
                                          str(self.PSK_input.text()) +
                                          '\n' + '\n' + 'Битовое представление: ' + '\n' + str(mes))
                self.reisiv_msg_bow.setText('Декодированное сообщение: '+ 
                                          str(decoded_msg) + 
                                          '\n' + '\n' + 'Битовое представление: ' + '\n' + str(arr_tmp_2))
            else:
                self.tmtr_msg_bow.setText('Тип модуляции: ' + M + '-PSK' + '\n' +
                                          'Битовое представление: ' + '\n' + str(mes))
                self.reisiv_msg_bow.setText('Битовое представление: ' + '\n' + str(arr_tmp_2))
                                 
            self.textBrowse_BER.setText("Ошибочных битов: " + str(ch) +
                                         "\nВсего битов: " + str(demod.__len__()) +
                                         "\nBER: " + str(float(ch)/float(demod.__len__()))
                                         )          
        
            self.progressBar_PSK.setValue(60)
            
            #Настройки для отрисовки графиков сигналов
            dmsg = demod
            dmsg_x = np.repeat(range(len(dmsg)), 2)
            dmsg_y = np.repeat(dmsg, 2)
            dmsg_x = dmsg_x[1:]
            dmsg_y = dmsg_y[:-1]
            dmsg_x = np.append(dmsg_x,dmsg_x[-1] + 1)
            dmsg_y = np.append(dmsg_y, dmsg_y[-1])
            
            mod_reals = [ele.real for ele in mod]
            n_mod_reals = [ele.real for ele in newMod]
            mod_imags = [ele.imag for ele in mod]
            n_mod_imags = [ele.imag for ele in newMod]
            
            if self.checkBox_show_sig_cons_psk.isChecked() == True:
                modem2.plot_const()
            
            self.progressBar_PSK.setValue(50)
            
            #Функции вызова отрисовки графиков
            draw_2(self, mes, demod)
            draw_11(self, msg_x, msg_y, "PSK")
            self.progressBar_PSK.setValue(75)
            draw_12(self, mod_reals, mod_imags, "PSK")
            self.progressBar_PSK.setValue(80)
            draw_13(self, dmsg_x, dmsg_y, "PSK")
            self.progressBar_PSK.setValue(90)
            draw_14(self, n_mod_reals, n_mod_imags, "PSK")
            
            self.progressBar_PSK.setValue(100)      
            
    #Обработчик проверки длины введенного сообщения     
    def signal_QAM_handler(self):
        check_input_QAM_len(self)
        
    #Обработчик проверки длины введенного сообщения            
    def signal_PSK_handler(self):
        check_input_PSK_len(self) 
        
    #Обработчик проверки на изменения введенного сообщения
    def PSK_input_change_handler(self):
        self.length_PSK_mes.setText(str(self.PSK_input.text().__len__()))
        check_input_PSK_len(self)    
    
    #Обработчик проверки на изменения введенного сообщения   
    def QAM_input_change_handler(self):
        self.length_QAM_mes.setText(str(self.QAM_input.text().__len__()))
        check_input_QAM_len(self)
    
    #Обработчик проверки коэф. мод. на изменение    
    def coef_QAM_handler(self):
        check_input_QAM_len(self)
    
    #Обработчик проверки коэф. мод. на изменение 
    def coef_PSK_handler(self):
        check_input_PSK_len(self) 

#Функция изменения подсказки при вводе сообщения
def check_input_QAM_len(self):
    M = int(self.combobox_coef_QAM.currentText())
    if self.combobox_signal_type_QAM.currentText() == 'Message with letters':
        self.hint_QAM.setText('Длина может быть: ' + 'любой')
        if (self.combobox_coef_QAM.currentText() == "64"):
            self.hint_QAM.setText('Длина должна быть: ' + 'кратна 6')
        if (self.combobox_coef_QAM.currentText() == "256"):
            self.hint_QAM.setText('Длина должна быть: ' + 'кратна 8')    
        # self.combobox_decision_QAM.setEnabled(False)
        
    if self.combobox_signal_type_QAM.currentText() == 'Binary code':
        self.hint_QAM.setText('Длина должна быть кратна: ' + str(int(np.log2(M))) + ", словарь: только 0 и 1")
        # self.combobox_decision_QAM.setEnabled(True)
        
    if self.combobox_signal_type_QAM.currentText() == 'Only integers':
        self.hint_QAM.setText('Длина может быть: ' + 'любой, максимальное число словаря не должно превышать: ' + str(M+1))
        # self.combobox_decision_QAM.setEnabled(False)
        
    if self.QAM_input.text() == "":
        self.hint_QAM.setText('СООБЩЕНИЕ НЕ МОЖЕТ БЫТЬ ПУСТЫМ!')
        print("void QAM inp")   

#Функция изменения подсказки при вводе сообщения               
def check_input_PSK_len(self):  
    M = int(self.combobox_coef_PSK.currentText())
    if self.combobox_signal_type_PSK.currentText() == 'Message with letters':
        self.hint_PSK.setText('Длина может быть: ' + 'любой')
        if (self.combobox_coef_PSK.currentText() == "32"):
            self.hint_PSK.setText('Длина должна быть: ' + 'кратна 5')
        # self.combobox_decision_PSK.setEnabled(False)
        
    if self.combobox_signal_type_PSK.currentText() == 'Binary code':
        self.hint_PSK.setText('Длина должна быть кратна: ' + str(int(np.log2(M))) + ", словарь: только 0 и 1")
        # self.combobox_decision_PSK.setEnabled(True)
        
    if self.combobox_signal_type_PSK.currentText() == 'Only integers':
        self.hint_PSK.setText('Длина может быть: ' + 'любой, максимальное число словаря не должно превышать: ' + str(M-1))
        # self.combobox_decision_QAM.setEnabled(False)
        
    if self.PSK_input.text() == "":
        self.hint_PSK.setText('СООБЩЕНИЕ НЕ МОЖЕТ БЫТЬ ПУСТЫМ!')
        print("void PSK inp")
           
#Обработчик настроек типа сообщения
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

#Обработчик настроек типа сообщения
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

#Функции необходимые для отрисовки интерфейса
app = QApplication([])
window = MainFunc()
window.show()
app.exec()