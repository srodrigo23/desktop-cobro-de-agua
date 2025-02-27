from model.main import Model
from view.main import View

class HomeController:
  
  def __init__(self, model: Model, view: View):
    self.model = model
    self.view = view
    self.frame = self.view.frames['home']
    self.bind()

  def bind(self):
    self.frame.signout_btn.config(command=self.logout)
  
  def logout(self):
    self.model.auth.logout()
  
  def update_view(self):
    current_user = self.model.auth.current_user
    if current_user:
      username = current_user["username"]
      self.frame.greeting.config(text=f"Welcome, {username}")
    else:
      self.frame.greeting.config(text=f"")
  

    