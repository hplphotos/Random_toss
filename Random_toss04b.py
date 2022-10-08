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

#print(toss_results)
sum_tosses = 0
for j in toss_results:
	sum_tosses = sum_tosses + toss_results[j]
print('\nTosses made =', sum_tosses)

# Sort toss_results
# Create a list of the toss_results keys
lst = list (toss_results.keys())
lst.sort() #sort list in ascendig order
lst_tups = list()
toss_list_outcome = list()
for key in lst:
	#print (key, toss_results[key])
	lst_tups.append((key,toss_results[key]))
	toss_list_outcome.append(toss_results[key])
print('\nSorted outcome list\n',lst_tups)
print(toss_list_outcome)

# Chi-square calculation. Set critical value
# The critical value is the value for which 5% of the area under the curve
# is in the right tail. This assumes n-1 degrees of freedom.
critical_chi_sq = 11.070

# Expected value of each of six outcomes
expected_val=sum_tosses/6.
chi_calc_numerator = 0
for i in toss_list_outcome:
	chi_calc_numerator = chi_calc_numerator + (i - expected_val) * (i - expected_val)
chi_sq = chi_calc_numerator/expected_val

# compare calculation with critical value from chi-square table
if chi_sq < critical_chi_sq:
	print('\n\tCan NOT reject the null hypothesis')
else:
	print('\n\tNull hypothesis REJECTED!')
print ('\tchi_sq =',chi_sq,' and the critical value =',critical_chi_sq)
