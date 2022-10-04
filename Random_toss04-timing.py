from Random_toss_classes import polyhedron,die1
import time

start_time = time.time()

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

#output execution time
print("--- %s seconds ---" % (time.time() - start_time))
