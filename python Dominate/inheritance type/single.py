class vehicle:
  def __init__(self,nm):
    self.name=nm

class bike(vehicle):

  def __init__(self, nm):
    super().__init__(nm)

  def display(self):
    
    print(f"the name of vehicle {self.name}") 


b1=bike("Honda")
b1.display()