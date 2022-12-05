def draw_12(self, mod_reals, mod_imags, type_modul):
    self.plot_area_wid_22.canvas.axes.clear()
    self.plot_area_wid_22.canvas.axes.scatter(mod_reals, mod_imags)
    self.plot_area_wid_22.canvas.axes.set_title("Комплексное представление переданного сообщения")
    self.plot_area_wid_22.canvas.axes.set_xlabel('Реальная часть')
    self.plot_area_wid_22.canvas.axes.set_ylabel('Мнимая часть')
    self.plot_area_wid_22.canvas.axes.grid()
    if type_modul == "PSK":
        self.plot_area_wid_22.canvas.axes.set_xlim(-1.1,1.1)
        self.plot_area_wid_22.canvas.axes.set_ylim(-1.1,1.1)
    self.plot_area_wid_22.canvas.draw()