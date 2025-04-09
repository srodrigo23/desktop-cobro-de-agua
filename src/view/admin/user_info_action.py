from customtkinter import CTkFrame, CTkLabel, CTkButton

class UserInfoAction(CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # self.lbl_user = CTkLabel(master=self, text="Usuario :", compound='left')
        # self.lbl_user.grid(row=0, column=0)

        self.lbl_user_name = CTkLabel(master=self, text="Miriam Lucana")
        self.lbl_user_name.grid(row=0, column=0)

        # self.lbl_user_type = CTkLabel(master=self, text="T. Usuario :")
        # self.lbl_user_type.grid(row=1, column=0)
        
        self.lbl_user_type_name = CTkLabel(master=self, text="ADMINISTRADOR")
        self.lbl_user_type_name.grid(row=1, column=0)

        self.btn_close_session = CTkButton(
            master=self, 
            fg_color='red', 
            text="Cerrar Sesión", 
            hover_color=('#f43939', '#fefefe'))
        self.btn_close_session.grid(row=2, column=0,pady=5, padx=5)
 