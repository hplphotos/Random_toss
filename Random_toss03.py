from __future__ import absolute_import, division, print_function
try:
     input = raw_input
except NameError:
     pass
#
# Create Proto-class from which all other classes descend.
#
from Random_toss_classes import Polyhedron,Die
print("Type is ",Die.poly_type,"\nNumber of sides is ",Die.numb_sides, "\n\n")
d=Die()
print("Result of throw is ",d.throw())