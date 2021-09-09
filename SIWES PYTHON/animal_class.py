class Animals:
    def __init__(self, name, FeedingMode, Leg, habitat):
         self.name = name
         self.FeedingMode = FeedingMode
         self.Leg = Leg
         self.habitat = habitat
         
         print(f"THE ANIMAL IS {self.name}")
         
    def housing(self):
           print(f"A {self.name} lives on {self.habitat}")
    def LegNo(self):
        print(f"A {self.name} has {self.Leg} legs")
    def Reproduction(self):
        print(f"A {self.name} reproduce sexually")
    def Classification(self):
        print(f"A {self.name} is a vertebrate animals")
        
FirstAnimal = Animals("dog", "carnivores", 4, "land")
SecondAnimal = Animals("cat", "carnivores", 4, "land")


FirstAnimal.housing()
SecondAnimal.housing()

FirstAnimal.LegNo()
SecondAnimal.LegNo()
 

class Fish:
    def __init__(self, name, FeedingMode, Leg, habitat):
          Animals. __init__(self, name, FeedingMode, Leg, habitat)
    def LegNo(self):
        print(f"A {self.name} has only fins not legs")
    def housing(self):
           print(f"A {self.name} lives in water")
    def Reproduction(self):
        print(f"A {self.name} reproduce sexually by laying eggs")
    def Classification(self):
        print(f"A {self.name} is a cartilaginous/vertebrate animals")
ThirdAnimal = Fish("fish", "carnivores", 0, "water") 

ThirdAnimal.housing()
ThirdAnimal.LegNo()
FirstAnimal.Reproduction()
SecondAnimal.Reproduction()
ThirdAnimal.Reproduction()
     


FirstAnimal.Classification()
SecondAnimal.Classification()
ThirdAnimal.Classification()
