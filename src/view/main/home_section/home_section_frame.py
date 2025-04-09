from customtkinter import CTkFrame

class HomeSectionFrame(CTkFrame):


    def __init__(self, master, **kwargs):
        
        super().__init__(master, **kwargs)

        # self.content_frame = CTkFrame(
        #     self,
        #     # fg_color='yellow'
        #     border_color='white',
        #     # border_width=1
        # )

        

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame1 = CTkFrame(
            self, 
            # fg_color='blue'
        )

        self.frame1.grid(row=0, column=0, padx=20, pady=20,sticky="nsew")

        self.frame2 = CTkFrame(
            self, 
            # fg_color='blue'
        )
        self.frame2.grid(row=0, column=1, padx=20, pady=20,sticky="nsew")

        self.frame3 = CTkFrame(
            self, 
            # fg_color='blue'
        )
        self.frame3.grid(row=1, column=0, padx=20, pady=20,sticky="nsew")

        self.frame4 = CTkFrame(
            self, 
            #  fg_color='blue'
        )
        self.frame4.grid(row=1, column=1, padx=20, pady=20,sticky="nsew")