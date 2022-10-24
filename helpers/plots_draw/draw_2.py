import numpy as np
def draw_2(self, mes, demod):
    self.plot_area_wid.canvas.axes.clear()
    self.plot_area_wid.canvas.axes.plot(abs(np.subtract(mes,demod)))
    self.plot_area_wid.canvas.axes.set_title("Subtract original signal and demodulated signal")
    self.plot_area_wid.canvas.axes.set_xlabel('t, s')
    self.plot_area_wid.canvas.axes.set_ylabel('A, V')
    self.plot_area_wid.canvas.axes.grid()
    self.plot_area_wid.canvas.draw()
