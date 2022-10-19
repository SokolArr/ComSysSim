import numpy as np
from ModulationPy import PSKModem

modem = PSKModem(4, np.pi/4,
                 gray_map=True,
                 bin_input=True)

modem.plot_const()