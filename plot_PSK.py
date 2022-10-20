import random
import numpy as np
from ModulationPy import PSKModem

def runEnginePSK (message, M_coef, noise_coef, phase, grey_cod, bin_inp, soft_decis, bin_out):
    
    print (' ')
    print ('Engine PSK Runs!')
    print('message:', message)
    print('M_coef:', M_coef)
    print('noise_coef:', noise_coef)
    print('phase:', phase)
    print('grey_cod:', grey_cod)
    print('bin_inp:', bin_inp)
    print('soft_decis:', soft_decis)
    print('bin_out:', bin_out)
    
    new_phase = np.pi / phase
    modem = PSKModem(M_coef, new_phase, grey_cod, bin_inp, soft_decis, bin_out)
    
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
    
    print ('Engine PSK Stopped!')
    
    # modem.plot_const()
    
    return modulated, new_modulated, demodulated, modem
    
