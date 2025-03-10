from tkinter import Tk

class Root(Tk):
  
  
  def __init__(self):
    super().__init__()

    title = 'OTB MIRAFLORES - CONTROL DE RECAUDACIONES'

    start_width = 700
    min_width = 700
    start_height = 400
    min_height = 400

    self.geometry(f"{start_width}x{start_height}")
    self.minsize(width=min_width, height=min_height)
    self.resizable(width=False, height=False)
    self.title(title)
    
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)