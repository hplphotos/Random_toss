import random
#
# Create Proto-class from which all other classes descend.
#
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
#
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

# Create class die1
#          
class die1(polyhedron):
     
     def __init__(self):
          polyhedron.__init__(self)
          self.outcome = 7
     poly_type = "die"
     numb_sides = 6
    
     def throw(self):
          self.outcome = random.randint(1,die1.numb_sides)
          return self.outcome
          
# end of class die1

# Create Class dice

class dice:
	poly_type = "dice"
	numb_sides = 12
#
	def __init__(self):
    		self.outcome=[0,0]
    		self.d1=die1()
#
	def throw(self):
		a=self.d1.throw()
		b=self.d1.throw()
		self.outcome = [a,b]
		return self.outcome
		
		     
     
        