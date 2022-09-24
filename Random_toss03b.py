from Random_toss_classes import polyhedron,die1
#

the_type = die1.poly_type
sides=die1.numb_sides

print("Type is ",the_type,"\nNumber of sides is ",sides, "\n\n")
d=die1()
print("Result of throw is ",d.throw())
