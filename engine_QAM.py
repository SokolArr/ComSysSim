import os
import random

import numpy as np
from ModulationPy import QAMModem

import matplotlib.pyplot as plt


modem = QAMModem(8, 
                 bin_input=False,
                 soft_decision=False,
                 bin_output=False)

msg = np.array([0, 0, 0, 1, 1, 0, 1, 1]) # input message

msg_x = np.repeat(range(len(msg)), 2)
msg_y = np.repeat(msg, 2)
msg_x = msg_x[1:]
msg_y = msg_y[:-1]
msg_x = np.append(msg_x,msg_x[-1] + 1)
msg_y = np.append(msg_y, msg_y[-1])


os.system('clear')

modulated = modem.modulate(msg) # modulation

print(str(modulated))

new_modulated = np.copy(modulated)


    


for index in range(new_modulated.size):
    # new_modulated[index].real = modulated[index].real + random.randint(0, 10)/100
    # new_modulated[index].imag = modulated[index].imag + random.randint(0, 10)/100
    new_modulated[index] = new_modulated[index] + (random.randint(0, 10)/100 + random.randint(0, 10)/100j)
    

print(str(new_modulated))




demodulated = modem.demodulate(new_modulated) # demodulation
dmsg = demodulated

dmsg_x = np.repeat(range(len(dmsg)), 2)
dmsg_y = np.repeat(dmsg, 2)
dmsg_x = dmsg_x[1:]
dmsg_y = dmsg_y[:-1]
dmsg_x = np.append(dmsg_x,dmsg_x[-1] + 1)
dmsg_y = np.append(dmsg_y, dmsg_y[-1])


# print("Modulated message:\n"+str(modulated))
# print("Demodulated message:\n"+str(demodulated)) 

# draw complex modulated
# extract real part
mod_reals = [ele.real for ele in modulated]
n_mod_reals = [ele.real for ele in new_modulated]
# extract imaginary part
mod_imags = [ele.imag for ele in modulated]
n_mod_imags = [ele.imag for ele in new_modulated]

# fig, axs = plt.subplots(3)
fig, axs = plt.subplots(1, 3, figsize=(10, 4.5), dpi = 90)
fig.tight_layout()

# fig.suptitle('msg and modulated signal')
fig.canvas.manager.set_window_title('Graph 1')

axs[0].plot(msg_x, msg_y, msg, 'ro')
axs[0].set_title('Сигнал (сообщение)')
axs[0].set_xlabel('t')
axs[0].set_ylabel('Амплитуда')


axs[1].scatter(mod_reals, mod_imags)
axs[1].set_title('Модулированный сигнал')
axs[1].set_xlabel('Реальная часть')
axs[1].set_ylabel('Мнимая часть')
axs[1].grid()
axs[1].set_xlim(-1,1)
axs[1].set_ylim(-1,1)

axs[1].scatter(n_mod_reals, n_mod_imags)
# axs[1].set_title('Модулированный сигнал c ошибками среды распр.')
axs[1].set_xlabel('Реальная часть')
axs[1].set_ylabel('Мнимая часть')
axs[1].set_xlim(-1,1)
axs[1].set_ylim(-1,1)

axs[1].legend(['Модулированный сигнал','Модулированный сигнал c ошибками среды распр.'])

axs[2].plot(dmsg_x, dmsg_y, demodulated, 'ro')
axs[2].set_title('Демодулированный сигнал')
axs[2].set_xlabel('t')
axs[2].set_ylabel('Амплитуда')

plt.show()




# fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
# ax1.plot(modulated,'o-')
# ax2.plot(new_modulated,'o-')

# plt.show()
