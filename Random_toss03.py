import Random_toss_classes

# from Random_toss_classes import Polyhedron,Die
#

the_type =  Random_toss_classes.die.poly_type
sides=Random_toss_classes.die.numb_sides

print("Type is ",the_type,"\nNumber of sides is ",sides, "\n\n")
d=Random_toss_classes.die()
print("Result of throw is ",d.throw())
