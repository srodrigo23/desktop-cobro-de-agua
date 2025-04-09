from tkinter import Frame
from customtkinter import CTkFrame
from .navigation.navigation import Navigation
from .home_section.home_section_frame import HomeSectionFrame
from .water_consumption_section.water_consumption_frame import WaterConsumtionFrame

class HomeView(Frame):
  def __init__(self, *args, **kwargs):
  
    super().__init__(*args, **kwargs)
    
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    self.menu_frame =  Navigation(
      self, 
      width=60,
      # border_color='white',
      # border_width=1
    )
    self.menu_frame.grid(row=0, column=0, sticky="ns")
    
    # pos=1
    # self.menu_frame.grid_rowconfigure(1, weight=1)
    # self.menu_frames[1] = CTkButton(self.menu_frame,width=100 , fg_color='green', command=lambda:self.callback(pos=1))
    # # self.menu_frames[i].bind("<Button-1>", lambda e:self.callback(event=e, pos=i))
    # self.menu_frames[1].grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    # self.section = HomeSectionFrame(self)
    self.section = WaterConsumtionFrame(master=self)
    self.section.grid(row=0, column=1, sticky="nsew")

