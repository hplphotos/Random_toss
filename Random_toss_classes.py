from __future__ import absolute_import, division, print_function
try:
     input = raw_input
except NameError:
     pass
import random
#
# Create Proto-class from which all other classes descend.
#
class Polyhedron:
	'''Polyhedron is a proto-class for creating sub-objects
	that can be used for random outcomes. Examples are coins,
	die, roulette, draedle, and playing card.
	There are two class variables:
	poly_type (str) for describing the sub-orject (coin, die, etc.)
	numb_sides (int) which is the number of sides of the object 
		e.g., 2 for coin, 6 for a die
	There is an instance variable (outcome) that stores the result
	of the throw memthod.
	There are also two methods, an _init__ and a throw method.
	The throw method generates a random int between 1 and mumb_sides
	'''
     poly_type = "poly"
     numb_sides = 1
     def __init__(self):
        self.outcome=0

     def throw(self):
          self.outcome = random.randint(1,polyhedron.numb_sides)
          return self.outcome
          
# end of class Polyhedron

# Create class Die
class Die(Polyhedron):
	'''
	The Die object has 6 sides.
	'''
     def __init__(self):
          Polyhedron.__init__(self)
          self.outcome = [7,'seven']
     poly_type = "die"
     numb_sides = 6
    
     def throw(self):
     	'''
     	The throw method generates a two element list as the outcome variable
		[random int between 1 and numb_sides, name of outcome(str)
     	'''
          outcome_names = ('one','two','three','four','five','six')
          self.outcome[0] = random.randint(1,Die.numb_sides)
          self.outcome[1] = outcome_names[self.outcome[0]-1]
          return self.outcome



  

