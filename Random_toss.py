from __future__ import absolute_import, division, print_function
try:
     input = raw_input
except NameError:
     pass
import random
#
# Create Proto-class from which all other classes descend.
#
class polyhedron:
#
# class attributes
#
    poly_type = "poly"
    numb_sides = 1
    def __init__(self):
        self.outcome=0
#
#This def of throw works, but I'd like to set outcome at the same time
    def throw(self):
         return random.randint(1,polyhedron.numb_sides)

# end of class polyhedron

# Create class die
class die(polyhedron):
     def __init__(self):
          polyhedron.__init__(self)
     poly_type = "die"
     numb_sides = 6

print("Type is ",die.poly_type,"\nNumber of sides is ",die.numb_sides, "\n\n")
d=die()
print("The outcome is ",d.outcome)
d.outcome=d.throw()
print("The outcome is ",d.outcome)
print("Result of throw is ",d.throw())

  

