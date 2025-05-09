
from model.main import Model
from view.main_view import View
from controller.main import Controller

def main():
    model = Model()
    view = View()
    view.start_mainloop()
    controller = Controller(model, view)
    controller.start()

if __name__ == "__main__":
    main()