from tkinter import Frame, Label, Button

from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkComboBox, StringVar, CTkScrollableFrame
from tkinter import Tk, font, Spinbox, Listbox, Scrollbar
from tkinter.ttk import LabelFrame

class HomeView(Frame):
  def __init__(self, *args, **kwargs):
  
    super().__init__(*args, **kwargs)
    
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    self.menu_frame =  CTkFrame(self,  fg_color='red',)
    self.menu_frame.grid(row=0, column=0, sticky="ns")
    
    self.menu_frames = [None]*5

    # for i in range(len(self.menu_frames)):
    pos = 0
    self.menu_frame.grid_rowconfigure(pos, weight=1)
    self.menu_frames[pos] = CTkButton(self.menu_frame,width=100 , fg_color='green', command=lambda:self.callback(pos=pos))
    self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")

    pos = 1
    self.menu_frame.grid_rowconfigure(pos, weight=1)
    self.menu_frames[pos] = CTkButton(self.menu_frame,width=100 , fg_color='red', command=lambda:self.callback(pos=pos))
    self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")

    pos = 2
    self.menu_frame.grid_rowconfigure(pos, weight=1)
    self.menu_frames[pos] = CTkButton(self.menu_frame,width=100 , fg_color='yellow', command=lambda:self.callback(pos=pos))
    self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")

    pos = 3
    self.menu_frame.grid_rowconfigure(pos, weight=1)
    self.menu_frames[pos] = CTkButton(self.menu_frame,width=100 , fg_color='white', command=lambda:self.callback(pos=pos))
    self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")

    pos = 4
    self.menu_frame.grid_rowconfigure(pos, weight=1)
    self.menu_frames[pos] = CTkButton(self.menu_frame,width=100 , fg_color='orange', command=lambda:self.callback(pos=pos))
    self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")
    
    pos=1

      # self.menu_frame.grid_rowconfigure(1, weight=1)
      # self.menu_frames[1] = CTkButton(self.menu_frame,width=100 , fg_color='green', command=lambda:self.callback(pos=1))
      # # self.menu_frames[i].bind("<Button-1>", lambda e:self.callback(event=e, pos=i))
      # self.menu_frames[1].grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    self.content_frame = CTkFrame(self, fg_color='yellow')
    # self.content_frame.grid(row=0, column=1, sticky="nsew")

    self.content_frame.grid_columnconfigure(0, weight=1)
    self.content_frame.grid_columnconfigure(1, weight=1)
    self.content_frame.grid_rowconfigure(0, weight=1)
    self.content_frame.grid_rowconfigure(1, weight=1)


    self.frame1 = CTkFrame(self.content_frame, fg_color='blue')

    self.frame1.grid(row=0, column=0, padx=20, pady=20,sticky="nsew")

    self.frame2 = CTkFrame(self.content_frame, fg_color='blue')
    self.frame2.grid(row=0, column=1, padx=20, pady=20,sticky="nsew")

    self.frame3 = CTkFrame(self.content_frame, fg_color='blue')
    self.frame3.grid(row=1, column=0, padx=20, pady=20,sticky="nsew")

    self.frame4 = CTkFrame(self.content_frame, fg_color='blue')
    self.frame4.grid(row=1, column=1, padx=20, pady=20,sticky="nsew")


    # self.header = Label(self, text="Home")
    # self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    # self.greeting = Label(self, text="sikik")
    # self.greeting.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    # self.signout_btn = Button(self, text="Sign Out")
    # self.signout_btn.grid(row=2, column=0, padx=10, pady=10)


    ################
    #    
    # PANEL DE COBRO DE AGUA
    # 
    ################

    self.water_billing_frame = CTkFrame(self, fg_color='pink')
    self.water_billing_frame.grid(row=0, column=1, sticky="nsew")

    self.water_billing_frame_title_label = CTkLabel(
      self.water_billing_frame, 
      text="Cobro de Agua",
      font=('American Typewriter', 40)

    )
    self.water_billing_frame_title_label.grid(row=0, column=0, sticky="nsew")
    
    combobox_var = StringVar(value="option 2")
    self.combobox = CTkComboBox(
      self.water_billing_frame, values=list( font.families()),
      command=self.combobox_callback, 
      variable=combobox_var
    )
    self.combobox.grid(row=1, column=0, sticky="nsew")
    self.spinnerbox = Spinbox(
      self.water_billing_frame, 
      from_=0, to=100, 
      command=self.spinnerbox_callback
    )
    self.spinnerbox.grid(row=1, column=2, sticky="nsew")

    self.lf_clients_list = LabelFrame(
      self.water_billing_frame,
      text="Lista de vecinos",
    )
    self.lf_clients_list.grid(row=2, column=1, sticky="nsew")

    self.lst_box_neighbors_list = Listbox(self.lf_clients_list)
    self.lst_box_neighbors_list.insert(1, "Python")
    self.lst_box_neighbors_list.insert(2, "Perl")
    self.lst_box_neighbors_list.insert(3, "C")

    self.lst_box_neighbors_list.pack()

    ###########
    #
    # Scroll bar oof frames
    # 
    ###########
    scrollable_frame =  ScrollableFrame(master=self.water_billing_frame)
    scrollable_frame.grid(row=2, column=2, sticky="nsew")
  
  def spinnerbox_callback(self):
    self.water_billing_frame_title_label.configure(font = ('American Typewriter', int(self.spinnerbox.get())))
    print("combobox dropdown clicked:", self.spinnerbox.get())

  def combobox_callback(self, choice):
    print("combobox dropdown clicked:", choice)

  def callback(self, pos):
    print ("clicked at", pos)



class ScrollableFrame(CTkScrollableFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)

    # add widgets onto the frame...
    for i in range(20):
      frame = Frame(self, height=20, 
                    bg='green'
                    )
      frame.widget="frame_"+str(i)
      frame.bind("<Button-1>", self.click_frame)
      frame.grid(
        row=i, column=0, pady=4, sticky="nsew",
      )
      CTkLabel(frame, text=f"This is a user frame {i}").grid(row=0, column=1, padx=20)
  def click_frame(self, event):
    widget = event.widget.widget
    print(widget)
    for i in self.winfo_children():
      print(i)
    # reference = self.nametowidget(widget)
    # reference.config(bg='red')



class CustomCTKFrame(CTkFrame):
  
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight=1)

#         self.my_frame = MyFrame(master=self, width=300, height=200, corner_radius=0, fg_color="transparent")
#         self.my_frame.grid(row=0, column=0, sticky="nsew")


# app = App()
# app.mainloop()

def main():
  pass

