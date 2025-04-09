from model.main import Model
from model.auth import Auth
from view.main_view import View

from .home import HomeController
from .login import LoginController
from .signup import SignUpController

class Controller:
  def __init__(self, model: Model, view: View) -> None:
    self.view = view
    self.model = model
    self.signin_controller = LoginController(model, view)
    # self.signup_controller = SignUpController(model, view)
    self.home_controller = HomeController(model, view)

    # self.model.auth.add_event_listener(
    #   "auth_changed", self.auth_state_listener
    # )

  def auth_state_listener(self, data:Auth) -> None:
    if data.is_logged_in:
      self.home_controller.update_view()
      self.view.switch("home")
    else:
      self.view.switch("signin")

  def start(self) -> None:
    if self.model.auth.is_logged_in:
      self.view.switch("home")
    else:
      self.view.switch("login")
    self.view.start_mainloop()