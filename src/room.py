# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = None 
    self.s_to = None 
    self.e_to = None 
    self.w_to = None
    self.items = []
  # def listItems(self, items):
  #   for i in items:
  #     print(i)
  def get_items(self):
    for i in self.items:
      print(i)

  def __str__(self):
      return f"Your Location: {self.name} - {self.description}"