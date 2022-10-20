import random
import numpy as np
from ModulationPy import QAMModem

def runEngineQAM (message, M_coef, noise_coef, grey_cod, bin_inp, soft_decis, bin_out):
    
    print (' ')
    print ('Engine QAM Runs!')
    print('message:', message)
    print('M_coef:', M_coef)
    print('noise_coef:', noise_coef)
    print('grey_cod:', grey_cod)
    print('bin_inp:', bin_inp)
    print('soft_decis:', soft_decis)
    print('bin_out:', bin_out)
   
    modem = QAMModem(M_coef, grey_cod, bin_inp, soft_decis, bin_out)
    
    # rand_list=[]
    # n=10
    
    # for i in range(n):
    #     rand_list.append(random.randint(0,3))

    msg = np.array(message)
    # print (msg)
    
    modulated = modem.modulate(msg) # modulation
    new_modulated = np.copy(modulated)
    
    for index in range(new_modulated.size):
        new_modulated[index] = new_modulated[index] + (random.randint(0, noise_coef)/100 + random.randint(0, noise_coef)/100j)
    
    # print(new_modulated)
    
    demodulated = modem.demodulate(new_modulated) # demodulation
    
    # print(demodulated)
    
    print ('Engine QAM Stopped!')
    
    return modulated, new_modulated, demodulated, modem
    

# def drawPSK(modulated, new_modulated, msg_x, msg_y, dmsg_x, dmsg_y):
#     #draw complex modulated
#     # extract real part
#     mod_reals = [ele.real for ele in modulated]
#     n_mod_reals = [ele.real for ele in new_modulated]
#     # extract imaginary part
#     mod_imags = [ele.imag for ele in modulated]
#     n_mod_imags = [ele.imag for ele in new_modulated]

#     # fig, axs = plt.subplots(3)
#     fig, axs = plt.subplots(1, 2, figsize=(10, 4.5), dpi = 90)
#     fig.tight_layout()

#     # fig.suptitle('msg and modulated signal')
#     fig.canvas.manager.set_window_title('Graph 1')

#     axs[0].plot(msg_x, msg_y,)
#     axs[0].set_title('Сигнал (сообщение) и демодулированный сигнал')
#     axs[0].set_xlabel('t')
#     axs[0].set_ylabel('Амплитуда')


#     axs[1].scatter(mod_reals, mod_imags)
#     axs[1].set_title('Комплексное представление сигнала')
#     axs[1].set_xlabel('Реальная часть')
#     axs[1].set_ylabel('Мнимая часть')
#     axs[1].grid()
#     # axs[1].set_xlim(-1,1)
#     # axs[1].set_ylim(-1,1)

#     axs[1].scatter(n_mod_reals, n_mod_imags)

#     axs[1].legend(['Модулированный сигнал, идеальная среда','Модулированный сигнал c ошибками среды распр.'])

#     axs[0].plot(dmsg_x, dmsg_y,)

#     axs[0].legend(['Сигнал (сообщение)','Демодулированный сигнал'])

#     plt.show()