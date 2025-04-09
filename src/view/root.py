from tkinter import Tk

class Root(Tk):
  
  def __init__(self):
    super().__init__()
    title = 'Sistema de Control OTB Miraflores'
    start_width = 1000
    min_width = 1000
    start_height = 800
    min_height = 800
    # TODO: crear la ventana que toda la pantalla
    self.geometry(f"{start_width}x{start_height}")
    self.minsize(width=min_width, height=min_height)
    self.resizable(width=True, height=True)
    self.title(title)
    # self.eval('tk::PlaceWindow . center')
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)