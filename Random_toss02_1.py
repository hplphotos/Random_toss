import random,sys

# Create Proto-class from which all other classes descend.

class polyhedron:
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
          self.outcome = [7,'seven']
     poly_type = "die"
     numb_sides = 6
    
     def throw(self):
          outcome_names = ('one','two','three','four','five','six')
          self.outcome[0] = random.randint(1,die.numb_sides)
          self.outcome[1] = outcome_names[self.outcome[0]-1]
          return self.outcome
# end of class die

print("\nType is ",die.poly_type,"\nNumber of sides is ",die.numb_sides, "\n")
d=die()
toss_result=d.throw()

print("Result of throw is",toss_result[0], "(",toss_result[1],")\n")
sys.exit("...exiting now")

  

