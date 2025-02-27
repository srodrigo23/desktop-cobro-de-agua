class ObservableModel:
  def __init__(self):
    self.event_listeners = {}
  
  def add_event_listener(self, event, fn):
    try:
      self.event_listeners[event].append(fn)
    except KeyError:
      self.event_listeners[event] = [fn]
    
    return lambda: self.event_listeners[event].remove(fn)
  
  def trigger_event(self, event):
    if event not in self.event_listeners.keys():
      return

    for func in self.event_listeners[event]:
      func(self)