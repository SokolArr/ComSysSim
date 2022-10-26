import numpy as np
def draw_2(self, mes, demod):
    self.plot_area_wid.canvas.axes.clear()
    self.plot_area_wid.canvas.axes.plot(abs(np.subtract(mes,demod)))
    self.plot_area_wid.canvas.axes.set_title("Разница между оригинальным сигналом и демодулированным")
    self.plot_area_wid.canvas.axes.set_xlabel('t, мс')
    self.plot_area_wid.canvas.axes.set_ylabel('Бит')
    self.plot_area_wid.canvas.axes.grid()
    self.plot_area_wid.canvas.draw()
