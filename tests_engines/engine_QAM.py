import os
import random

import numpy as np
from ModulationPy import QAMModem

import matplotlib.pyplot as plt

noise_coef = 1
modem = QAMModem(16, 
                 bin_input=True,
                 soft_decision=False,
                 bin_output=True)

# msg = np.array([0, 0, 0, 1, 1, 0, 1, 1]) # input message
# msg = np.array([1,2,3,2,1,2,1,1,0,2,3,1,0,0,0,2,3,0,0]) # input message
# msg = np.random.sample(10)

# rand_list=[]
# n=100

# for i in range(n):
#     rand_list.append(random.randint(0,3))

msg = np.array([1,1,0,1])

print (msg)

msg_x = np.repeat(range(len(msg)), 2)
msg_y = np.repeat(msg, 2)
msg_x = msg_x[1:]
msg_y = msg_y[:-1]
msg_x = np.append(msg_x,msg_x[-1] + 1)
msg_y = np.append(msg_y, msg_y[-1])


# os.system('clear')

modulated = modem.modulate(msg) # modulation

print (str(modulated))

# print(str(modulated))

new_modulated = np.copy(modulated)


    


for index in range(new_modulated.size):
    # new_modulated[index].real = modulated[index].real + random.randint(0, 10)/100
    # new_modulated[index].imag = modulated[index].imag + random.randint(0, 10)/100
    new_modulated[index] = new_modulated[index] + (random.randint(0, noise_coef)/100 + random.randint(0, noise_coef)/100j)

print (new_modulated)

# print(str(new_modulated))




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
fig, axs = plt.subplots(1, 2, figsize=(10, 4.5), dpi = 90)
fig.tight_layout()

# fig.suptitle('msg and modulated signal')
fig.canvas.manager.set_window_title('Graph 1')

axs[0].plot(msg_x, msg_y,)
axs[0].set_title('Сигнал (сообщение) и демодулированный сигнал')
axs[0].set_xlabel('t')
axs[0].set_ylabel('Амплитуда')


axs[1].scatter(mod_reals, mod_imags)
axs[1].set_title('Комплексное представление сигнала')
axs[1].set_xlabel('Реальная часть')
axs[1].set_ylabel('Мнимая часть')
axs[1].grid()
# axs[1].set_xlim(-1,1)
# axs[1].set_ylim(-1,1)

axs[1].scatter(n_mod_reals, n_mod_imags)

axs[1].legend(['Модулированный сигнал, идеальная среда','Модулированный сигнал c ошибками среды распр.'])

axs[0].plot(dmsg_x, dmsg_y,)

axs[0].legend(['Сигнал (сообщение)','Демодулированный сигнал'])

plt.show()




# fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
# ax1.plot(modulated,'o-')
# ax2.plot(new_modulated,'o-')

# plt.show()
