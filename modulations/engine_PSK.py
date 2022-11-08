import random
import numpy as np
from ModulationPy import PSKModem

def runEnginePSK (message, M_coef, mu, sigma, phase, grey_cod, bin_inp, soft_decis, bin_out):
    
    print (' ')
    print ('Engine PSK Runs!')
    print('message:', message)
    print('M_coef:', M_coef)
    print('mu:', mu)
    print('sigma:', sigma)
    print('phase:', phase)
    print('grey_cod:', grey_cod)
    print('bin_inp:', bin_inp)
    print('soft_decis:', soft_decis)
    print('bin_out:', bin_out)
    
    new_phase = np.pi / phase
    
    modem = PSKModem(M_coef, new_phase, grey_cod, bin_inp, soft_decis, bin_out)
    msg = np.array(message)
    
    modulated = modem.modulate(msg) # modulation
    new_modulated = np.copy(modulated)
    
    noise_real = np.random.normal(mu, sigma, len(msg))
    noise_imag = np.random.normal(mu, sigma, len(msg))
    
    for index in range(new_modulated.size):
        new_modulated[index] = new_modulated[index] + (noise_real[index] + noise_imag[index]*1j)

    demodulated = modem.demodulate(new_modulated) # demodulation
    
    print ('Engine PSK Stopped!')

    return modulated, new_modulated, demodulated, modem
    
