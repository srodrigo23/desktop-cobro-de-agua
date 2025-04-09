from model.main import Model
from model.auth import User
from view.main_view import View


class LoginController:

  def __init__(self, model: Model, view:View):
    self.model = model
    self.view = view
    self.frame = self.view.frames["login"]
    self.bind()

  def bind(self):
    self.frame.access_button.configure(command=self.login) #ctkbutton
    self.frame.cancel_button.configure(command=self.cancel_login)

  def close_app_after_time(self)->None:
    import time
    time.sleep(2)
    self.view.root.destroy()

  def cancel_login(self):
    print('cancel_login')
    self.frame.show_message_alerts()
    from threading import Thread
    t1 = Thread(target=self.close_app_after_time)
    t1.start()
    # t1.join()

  def login(self):
    print('login')
    username = self.frame.username_entry.get()
    pasword = self.frame.password_entry.get()
    data = {"username": username, "password": pasword}
    print(data) # of course we don't want to print the password in a real app!
    
    # self.frame.password_input.delete(0, last=len(pasword))
    # user: User = {"username": data["username"]}
    # self.model.auth.login(user)