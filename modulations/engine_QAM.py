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
    
    msg = np.array(message)
    
    modulated = modem.modulate(msg) # modulation
    new_modulated = np.copy(modulated)
    
    for index in range(new_modulated.size):
        new_modulated[index] = new_modulated[index] + (random.randint(0, noise_coef)/100 + random.randint(0, noise_coef)/100j)

    demodulated = modem.demodulate(new_modulated) # demodulation
    
    print ('Engine QAM Stopped!')
    
    return modulated, new_modulated, demodulated, modem