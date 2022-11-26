import numpy as np                  #Импорт библиотек
from ModulationPy import QAMModem   #Импорт библиотек

def runEngineQAM (message, M_coef, mu, sigma, grey_cod, bin_inp, soft_decis, bin_out):
    #Логгирование входных данных                        
    print (' ')
    print ('Engine QAM Runs!')
    print('message:', message)
    print('M_coef:', M_coef)
    print('mu:', mu)
    print('sigma:', sigma)
    print('grey_cod:', grey_cod)
    print('bin_inp:', bin_inp)
    print('soft_decis:', soft_decis)
    print('bin_out:', bin_out)
    
    #Инициализация QAM модема
    modem = QAMModem(M_coef, grey_cod, bin_inp, soft_decis, bin_out)
    
    #Подготовка массива данных из сообщения
    msg = np.array(message)
    
    #Запуск процесса модуляции
    modulated = modem.modulate(msg)
    new_modulated = np.copy(modulated)
    
    #Инициализация шумовых переменных
    noise_real = np.random.normal(mu, sigma, len(msg))
    noise_imag = np.random.normal(mu, sigma, len(msg))
    
    #Добавление шума
    for index in range(new_modulated.size):
        new_modulated[index] = new_modulated[index] + (noise_real[index] + noise_imag[index]*1j)
        
    #Запуск процесса демодуляции
    demodulated = modem.demodulate(new_modulated)
    
    print ('Engine QAM Stopped!')
    return modulated, new_modulated, demodulated, modem