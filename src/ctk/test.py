import customtkinter
import tkinter as tk
from PIL import Image
# from tk import PhotoImage


class App(customtkinter.CTk):
    def __init__(self):
      super().__init__()
      self.geometry("600x500")
      self.title("CTk example")

      # add widgets to app
      self.button = customtkinter.CTkButton(
        self, 
        command=self.button_click, 
        # image=tk.PhotoImage(file='resources/login_icon.png')
        image=customtkinter.CTkImage(
          light_image=Image.open("resources/login.png"),
          # dark_image=Image.open("<path to dark mode image>"),
          size=(30, 30),
        ),
        text="",
        width=10,
        height=10,
        bg_color='white'
      )
      self.button.grid(row=0, column=0, padx=20, pady=10)


    # add methods to app
    def button_click(self):
      print("button click")


app = App()
app.mainloop()