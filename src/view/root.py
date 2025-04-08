from tkinter import Tk

class Root(Tk):
  
  
  def __init__(self):
    super().__init__()

    title = 'Sistema de Control OTB Miraflores'

    start_width = 1000
    min_width = 1000
    start_height = 600
    min_height = 600

    self.geometry(f"{start_width}x{start_height}")
    self.minsize(width=min_width, height=min_height)
    # self.resizable(width=False, height=False)
    self.title(title)
    # self.eval('tk::PlaceWindow . center') # mala posicion
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)