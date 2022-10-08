from Random_toss_classes import polyhedron,die1

num_tosses = 6000000
toss_results = dict()
d = die1()
#
i = 1
while i <= num_tosses:
  the_toss = d.throw()
  if the_toss not in toss_results:
  	toss_results[the_toss] = 1
  else:
  	toss_results[the_toss] = toss_results[the_toss] + 1
  i += 1

print(toss_results)
sum_tosses = 0
for j in toss_results:
	sum_tosses = sum_tosses + toss_results[j]
print('Count of all tosses =', sum_tosses)

# Sort toss_results
# Create a list of the toss_results keys
lst = list (toss_results.keys())
lst.sort() #sort list in ascendig order
for key in lst:
	print (key, toss_results[key]) 

