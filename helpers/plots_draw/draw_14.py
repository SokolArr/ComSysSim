def draw_14(self, n_mod_reals, n_mod_imags, type_modul):
    self.plot_area_wid_24.canvas.axes.clear()
    self.plot_area_wid_24.canvas.axes.scatter(n_mod_reals, n_mod_imags)
    self.plot_area_wid_24.canvas.axes.set_title("Demodulated complex message")
    self.plot_area_wid_24.canvas.axes.set_xlabel('Real')
    self.plot_area_wid_24.canvas.axes.set_ylabel('Imag')
    self.plot_area_wid_24.canvas.axes.grid()
    if type_modul == "PSK":
        self.plot_area_wid_24.canvas.axes.set_xlim(-1.1,1.1)
        self.plot_area_wid_24.canvas.axes.set_ylim(-1.1,1.1)
    self.plot_area_wid_24.canvas.draw()