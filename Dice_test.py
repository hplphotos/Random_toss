from Random_toss_classes import dice

# Only need to import dice. Other classes create dice but are
# not needed in this program.
# from Random_toss_classes import polyhedron,die,die1,dice

the_type = dice.poly_type
sides=dice.numb_sides

print("Type is ",the_type,"\nNumber of sides is ",sides, "\n\n")

d=dice()
print("Result of throw is ",d.throw())
