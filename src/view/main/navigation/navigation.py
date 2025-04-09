from customtkinter import CTkFrame, CTkButton, CTkImage
from PIL import Image

from .user_info_action import UserInfoAction

class Navigation(CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.menu_frames = [None]*6
        pos = 0
        self.grid_rowconfigure(pos, weight=1)
        self.theme = {
            'hover_color': ('#13d1fc','#f3f8f9'),
            'font': ('Arial', 20),
            'fg_color':'white',
            'text_color':('black'),
        }

        self.menu_frames[pos] = CTkButton(
            self,
            width=80,
            command=lambda:self.callback(pos=pos),
            image=CTkImage(
                # light_image=Image.open("resources/home.png"),
                dark_image=Image.open("resources/home.png"),
                size=(40, 40),
            ),
            text='Principal',
            compound="top",
            font=self.theme['font'],
            fg_color=self.theme['fg_color'],
            text_color=self.theme['text_color'],
            hover_color=self.theme['hover_color']
        )
        self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")

        pos = 1
        self.grid_rowconfigure(pos, weight=1)
        self.menu_frames[pos] = CTkButton(
            self,
            width=100, 
            image=CTkImage(
                # light_image=Image.open("resources/home.png"),
                dark_image=Image.open("resources/water2.png"),
                size=(40, 40),
            ),
            text='Consumo\nde Agua',
            compound='top',
            font=self.theme['font'],
            fg_color=self.theme['fg_color'],
            text_color=self.theme['text_color'],
            hover_color=self.theme['hover_color'],
            state='disabled'
        )
        self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")

        pos = 2
        self.grid_rowconfigure(pos, weight=1)
        self.menu_frames[pos] = CTkButton(
            self,
            width=100, 
            # command=lambda:self.callback(pos=pos)
            image=CTkImage(
                light_image=Image.open("resources/paper.png"),
                # dark_image=Image.open("resources/water2.png"),
                size=(40, 40),
            ),
            text='Lecturación',
            compound='top',
            font=self.theme['font'],
            fg_color=self.theme['fg_color'],
            text_color=self.theme['text_color'],
            hover_color=self.theme['hover_color']
        )
        self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")

        pos = 3
        self.grid_rowconfigure(pos, weight=1)
        self.menu_frames[pos] = CTkButton(
            self,
            image=CTkImage(
                light_image=Image.open("resources/vecinos.png"),
                # dark_image=Image.open("resources/water2.png"),
                size=(40, 40),
            ),
            text='Vecinos',
            compound='top',
            font=self.theme['font'],
            fg_color=self.theme['fg_color'],
            text_color=self.theme['text_color'],
            hover_color=self.theme['hover_color']
        )
        self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")

        pos = 4
        self.grid_rowconfigure(pos, weight=1)
        self.menu_frames[pos] = CTkButton(
            self,
            image=CTkImage(
                light_image=Image.open("resources/money.png"),
                # dark_image=Image.open("resources/water2.png"),
                size=(40, 40),
            ),
            text='Recaudaciones',
            compound='top',
            font=self.theme['font'],
            fg_color=self.theme['fg_color'],
            text_color=self.theme['text_color'],
            hover_color=self.theme['hover_color']
        )
        self.menu_frames[pos].grid(row=pos, column=0, padx=10, pady=10, sticky="nsew")

        self.user_info_action = UserInfoAction(master=self)
        self.user_info_action.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
        