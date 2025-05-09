from .root import Root
from .main.home_view import HomeView
# from .signin import SignInView
# from .signup import SignUpView
from .login.login import Login

class View:
  def __init__(self):
    self.root = Root()
    self.frames = {
      # "login": Login,
      # "signup": SignUpView,
      # "home": HomeView,
    }
    # self.current_frame = self.frames['signin'](self.root)
    # self.current_frame.grid(row=0, column=0, sticky="nsew")
    # self.frames: Frames = {}  # type: ignore

    self._add_frame(Login, "login")
    # self._add_frame(SignInView, "signin")
    self._add_frame(HomeView, "home")

  def _add_frame(self, Frame, name):
    self.frames[name] = Frame(self.root)
    self.frames[name].grid(row=0, column=0, sticky="nswe")

  def switch(self, name):
    frame = self.frames[name]
    frame.tkraise()

    # new_frame = self.frames[name](self.root)
    # if self.current_frame is not None:
    #   self.current_frame.destroy()
    # self.current_frame = new_frame
    # self.current_frame.grid(row=0, column=0, sticky="nsew")

  def start_mainloop(self):
    self.root.mainloop()