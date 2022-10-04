# Random_toss
 
## Purpose of the Random_toss scripts

The Random_toss set of python scripts simulate tossing a multi-sided object and reporting which side was "up". The various tests are numbered sequentially starting with **Random_toss01.py**. Random_toss0 and Random_toss03a test the ability to save the class structure in a separate file, Random_toss_classes.py, and import it into another file. 

**Random_toss03** imports the entire classes file and then uses specific classes. This means that the name of the file must precede the reference to specific attributes and methods (the_type =  Random_toss_classes.die.poly_type).

On the other hand, **Random_toss03a** imports explicitly only the classes needed in this script. So references to specific attributes and methods do not need to be preceded by the file name (the_type = die.poly_type).

The program **Random_toss04** uses a dictionary to save the number of times each of the six outcomes occurs. Since I set the number of tosses to 6 million I was curious about the execution time. The version **Random_toss04-timing** is the same as the **Random_toss04** version except that it contains some code to measure the execution time.

## Multi-sided Objects

Multi-sided objects are objects you can toss in the air and one of their sides will be "on top". For example, a two-sided object, which we call a coin, can only result in a head or a tail. It is assumed that all multi-sided objects are unbiased, meaning that any of the sides are equally likely to come up on top. This is accomplished by using the Randint function from the Random module. I assume this function produces unbiased results, but it might be interesting to test it.

### Types of Multi-sided Objects

* A two-sided object is a coin. The outcome can only be heads or tails (random integers 1 or 2).
* A four-sided object is a dreidel. The outcome is one of the four Hebrew letters on the sides of the dreidel.
* A six-sided object is a die, while a pair of them are called a set of dice. Outcome of tossing a die is an integer from one to six.

## Current State of the Simulation

I've concentrated on the die class. One reason is that I'd like to simulate a game of baseball that I used to play with a pair of dice as a kid. Each outcome of tossing a pair of dice is mapped to a specific baseball occurrence, like a single, double, home run, strike out, etc. For example 2 & 2 is a double, 1 & 1 is a strikeout, 2 & 5 is a single, and 5 & 6 is a fly out.

Person A tosses the dice to simulate the top of the first inning. After three outs, Person B tosses the dice to simulate the bottom of the first inning. The players alternate turns until all nine innings are completed and a winner is determined by who had the most runs. The game can go on to extra innings if the score is tied after nine innings.

Another possible simulation is to throw a pair of dice thousands of times and record the number of times each of the 36 possible outcomes comes up. For an unbiased pair of dice the result should be an equal number of hits for each of the possible outcomes. For n tosses, each of the outcomes should happen, in theory, n/36 times. This simulation can be done with just one die and then each possible outcome could occur n/6 times. In either case, a chi-squared test could be used to test the randomness of the simulation.

## Execution Timing

Since Python is an interpreted language, I was curious about how long it would take to run a simulation with millions of trials (tosses of the die). The file Random_toss04-timing.py using the `time` module to measure the start and stop time of the execution of the die tossing program.

I set the number of tosses of the die to 6,000,000 and saved the start time. The last statement prints the difference between the end time and the start time in seconds. The result for the 6 million tosses, organized in a dictionary to save the results for each of the six possible outcomes, was about 6.4 seconds. This works out to just a bit over a million tosses in a second! This seems very fast for an interpreted language.


