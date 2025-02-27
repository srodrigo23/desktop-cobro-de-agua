from model.main import Model
from model.auth import User
from view.main import View


class SignInController:
  def __init__(self, model: Model, view:View):
    self.model = model
    self.view = view
    self.frame = self.view.frames["signin"]
    self.bind()

  def bind(self):
    self.frame.signin_btn.config(command=self.signin)
    self.frame.signup_btn.config(command=self.signup)

  def signup(self):
    print('this is a siginup')
    self.view.switch("signup")

  def signin(self):
    print('clicked signin')
    username = self.frame.username_input.get()
    pasword = self.frame.password_input.get()
    data = {"username": username, "password": pasword}
    print(data) # of course we don't want to print the password in a real app!
    self.frame.password_input.delete(0, last=len(pasword))
    user: User = {"username": data["username"]}
    self.model.auth.login(user)