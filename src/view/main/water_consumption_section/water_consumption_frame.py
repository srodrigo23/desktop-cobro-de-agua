
from customtkinter import CTkFrame, CTkLabel, StringVar, CTkComboBox, CTkScrollableFrame
from tkinter import Frame#, Label, Button
from tkinter import font, Spinbox, Listbox
from tkinter.ttk import LabelFrame

class WaterConsumtionFrame(CTkFrame):

    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)

        self.water_billing_frame_title_label = CTkLabel(
            self,
            text="Cobro de Agua",
            font=('American Typewriter', 40)
        )
        self.water_billing_frame_title_label.grid(row=0, column=0, sticky="nsew")
    
        combobox_var = StringVar(value="option 2")
        self.combobox = CTkComboBox(
            self, values=list(font.families()),
            command=self.combobox_callback, 
            variable=combobox_var
        )
        self.combobox.grid(row=1, column=0, sticky="nsew")
        self.spinnerbox = Spinbox(
          self, 
          from_=0, to=100, 
          command=self.spinnerbox_callback
        )
        self.spinnerbox.grid(row=1, column=2, sticky="nsew")

        self.lf_clients_list = LabelFrame(
            self,
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
        scrollable_frame = ScrollableFrame(master=self)
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