class Students:
    def __init__(self, name, age, gender, mat_no):
      self.name = name
      self.age = age
      self.gender = gender
      self.mat_no = mat_no
      self.level = "nd 1"

      print(f'My name is  {self.name} I am a student of FCAHPTIB')
      
  
    def payFees(self):
        print(f'{self.name} has paid the amount of 50,000 for {self.level}')

    def attendClass(self):
         print(f"{self.name} attended class regularly during {self.level}")
         
    def writeExaam(self):
        print(f"{self.name} writes examination for {self.level}")
        
student1 = Students("ADEMOLA", 12, "m", "NDCOM/19/303")
student2 =  Students("ABDULRAFIU", 32, "F", "NDCOM/19/303")
student3 = Students("ADEMOLA", 33, "MALE", "NDCOM/19/308")

student1.payFees()
student2.payFees()
student3.payFees()


student1.attendClass()
student2.attendClass()
student3.attendClass()


student1.writeExaam()
student2.writeExaam()
student3.writeExaam()



#INHERITANCE
class PartTimeStudents(Students):
  def __init__(self, name, age, gender, mat_no):
      Students.__init__(self, name, age, gender, mat_no)
  def payFees(self):
      print(f'{self.name} has paid the amount of 150,000 for {self.level}')
      
pt_student = PartTimeStudents("aishat", 22, "female", "NDCOM/19/333")


pt_student.writeExaam()
pt_student.attendClass()  
pt_student.payFees()

    
#ENCAPSULATION
#ABSTRACTION
#POLYMORPHISM
#polymorphism is when a function perform many task
  