def draw_11(self, msg_x, msg_y, type_modul):
    self.plot_area_wid_21.canvas.axes.clear()
    self.plot_area_wid_21.canvas.axes.plot(msg_x, msg_y)
    self.plot_area_wid_21.canvas.axes.set_title("Original message")
    self.plot_area_wid_21.canvas.axes.set_xlabel('t, s')
    self.plot_area_wid_21.canvas.axes.set_ylabel('A, V')
    self.plot_area_wid_21.canvas.axes.grid()
    self.plot_area_wid_21.canvas.draw()