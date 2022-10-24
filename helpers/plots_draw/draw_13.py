def draw_13(self, dmsg_x, dmsg_y, type_modul):
    self.plot_area_wid_23.canvas.axes.clear()
    self.plot_area_wid_23.canvas.axes.plot(dmsg_x, dmsg_y)
    self.plot_area_wid_23.canvas.axes.set_title("Demodulated message")
    self.plot_area_wid_23.canvas.axes.set_xlabel('t, s')
    self.plot_area_wid_23.canvas.axes.set_ylabel('A, V')
    self.plot_area_wid_23.canvas.axes.grid()
    self.plot_area_wid_23.canvas.draw()