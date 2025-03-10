
import tkinter as tk

from tkinter.ttk import Frame
from tkinter.ttk import Label, Entry, Button, LabelFrame
# from tkinter import PhotoImage

import customtkinter

from PIL import Image

class Login(tk.Frame):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setup()

  def setup(self)-> None:
    self.mainframe = LabelFrame(
      self,
      borderwidth=3, 
      relief="sunken",
    )
    # self.mainframe.config(text='INGRESO AL SISTEMA')
    
    self.mainframe.pack(
      side=tk.LEFT, 
      # fill=tk.BOTH, 
      # ipadx=50,
      # ipady=50,
      # ipady=10,
      expand=True
    )
    
    
    Label(self.mainframe, text="INGRESO AL SISTEMA", font=("Arial", 25, "bold"), ).pack(side=tk.TOP)
    # Label(self.mainframe, text="OTB Miraflores", font=("Arial", 16, "bold"), ).pack(side=tk.TOP)

    self.data_frame = Frame(self.mainframe)
    self.data_frame.pack(side=tk.TOP, pady=10)

    self.username_label = Label(self.data_frame, text="Usuario :")
    self.username_label.grid(row=0, column=0, sticky=tk.E, pady=2)
    self.password_label = Label(self.data_frame, text="Contraseña :")
    self.password_label.grid(row=1, column=0, sticky=tk.W, pady=2)
    
    self.username_entry = Entry(self.data_frame)
    self.username_entry.grid(row=0, column=1, columnspan=4, sticky='we', pady=5)
    self.password_entry = Entry(self.data_frame, show='*')
    self.password_entry.grid(row=1, column=1, columnspan=1, sticky=tk.W, pady=5)


    self.buttons_frame = Frame(self.mainframe)
    self.buttons_frame.pack(side=tk.TOP, fill=tk.BOTH, ipady=10)
  
    # self.access_button = Button(self.mainframe, text="INGRESAR")
    self.buttons_frame.columnconfigure(index=0, weight=1)
    self.buttons_frame.columnconfigure(index=1, weight=1)
    self.access_button = customtkinter.CTkButton(
      self.buttons_frame, 
      # command=self.button_click,
      image=customtkinter.CTkImage(
        light_image=Image.open("resources/login.png"),
        # dark_image=Image.open("<path to dark mode image>"),
        size=(20, 20),
      ),
      text="Ingresar",
      width=10,
      height=10,
      fg_color='green'
      # bg_color='white'
    )
    self.access_button.grid(row=0, column=0, padx=10, pady=0, sticky='we')

    self.cancel_button = customtkinter.CTkButton(
      self.buttons_frame, 
      # command=self.button_click,
      image=customtkinter.CTkImage(
        light_image=Image.open("resources/cancel_icon.png"),
        # dark_image=Image.open("<path to dark mode image>"),
        size=(20, 20),
      ),
      text="Cancelar",
      fg_color='red',
      width=10,
      height=10,
      # anchor='w'
      # bg_color='red'
    )
    self.cancel_button.grid(row=0, column=1, padx=10, pady=0, sticky='we')
    
    # self.access_button.pack(side=tk.LEFT, padx=20)
    # self.button.grid(row=0, column=0, padx=20, pady=10)


    
    # self.__access_button__.pack(side=tk.TOP, fill='both')
    # Button(self.__mainframe__, text='this is').grid(row=)



    # self.geometry("400x200")
    # self.config(bg='skyblue')
    # self.eval('tk::PlaceWindow . center')