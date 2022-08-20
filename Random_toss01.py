import random,sys

# Create Proto-class from which all other classes descend.

class polyhedron:

# class attributes

     poly_type = "poly"
     numb_sides = 1
     def __init__(self):
        self.outcome=0

     def throw(self):
          self.outcome = random.randint(1,polyhedron.numb_sides)
          return self.outcome
          
# end of class polyhedron

# Create class die
class die(polyhedron):
     def __init__(self):
          polyhedron.__init__(self)
     poly_type = "die"
     numb_sides = 6
     
     def throw(self):
          self.outcome = random.randint(1,die.numb_sides)
          return self.outcome

print("Type is ",die.poly_type,"\nNumber of sides is ",die.numb_sides, "\n")
d=die()
print("Result of throw is ",d.throw(),"\n")
sys.exit("...Exiting Random_Toss")

  

