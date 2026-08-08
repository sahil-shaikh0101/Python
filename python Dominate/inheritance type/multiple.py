# Ex:1

class Dancer:
  def fDancer(Self):
    print("i am fbase from Dancer")

class Trainer:
  def ftrainer(Self):
    print("i am ftrainer from Trainer")

class Dance_Trainer(Dancer,Trainer):
  def fdancerTrainer(self):
    print("I am DanceTrainer fromDAnceTrainer class  ")   

d1=Dance_Trainer()
d1.fDancer()
d1.ftrainer()
d1.fdancerTrainer( )

# Ex:2

class Doctor:
  def treat_patient(self):
    print("I treat patient")

class Researcher:
  def conduct_research(self):
    print("i reseach on patiant deisease")

class medicalscientist(Doctor,Researcher):
  def analyze_data(self):
    print("I analyze data of Doctor and Reseaecher") 

m1=medicalscientist()       
m1.treat_patient()
m1.conduct_research()
m1.analyze_data()

# Ex:3

class Engine:
  def start_engine(self):
    print("i start through using Engine")

class Gps:
  def show_location(self):
    print("I show actual location map for cars")    

class smartcar(Engine,Gps):
  def sefdrive(self):
    print("I am modern technology car i have self drive feature . so without driver i drive i dont need driver")    

s1=smartcar()    
s1.start_engine()
s1.show_location()
s1.sefdrive()

# Ex:-4

class Developer:
  def write_code(self):
    print("I write code ")

  def problem_solve(self):
    print("I solve bussiness problems") 

class Designer:
  def design_ui(self):
    print("I designer i design website UI")

class UI_Engineer(Developer,Designer):
  def build_interface(self):
    print("I build interface using help of developer and Designer.")

  def problem_solve(self):
   super().problem_solve()
   print("i help developer some time he need")

    
u1=UI_Engineer()  
u1.write_code()  
u1.design_ui()
u1.build_interface()
u1.problem_solve()


