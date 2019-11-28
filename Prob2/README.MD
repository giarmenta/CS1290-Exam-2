The Minimum Falling Path Sum 

1.	For this problem one must traverse the array of integers and add them. For example, when using a 3x3 square, one must add a digit from each row and get the lowest (minimum) sum as the answer with the constraint that it has to be at most 1 in difference.  The recursive function used is:
path = min(path, db[i + 1][j – 1])
path = min(path, db[i + 1][j +1])
This way the result is stored in the in the variable path. Once the variable is stored, this is stored in a 2D list and is added to the values of the list to get the sum of all possible paths. 

2.	The solution is stored in a 2D list as mentioned earlier. this is list is generated from traversing the 2nd and 3rd row with the test provided. The first row is stored for reference and form there all possible are checked with the constraint of each column have a difference of at most 1.

3.	IDEAL

I – Identify

This problem was challenging for me as I struggled to make sense of it. I understood the list needed to be traversed but needed to pinpoint the starting point and adding the at most 1 constraint.

D – Define

The problem is to get the lowest sum from a digit within each row.

E – Explore

The best option is to have a 2D list to store values of all the possible paths.

A – Act

I attempted various algorithms for this problem since the sums needed to be stored and not repeat themselves.

L – Learn

I look back at this problem and managed to learn a new way of solving this problem.

Duke’s 7 steps

1.	Pseudo code was done breaking down the problem step by step.

2.	With the example provided I attempted to work backwards to come up with the solution to this problem.

3.	This problem was difficult and it is why I got fixed into trying it. I didn’t manage to find a pattern for this problem.

4.	I traced the solution back and forth to understand the algorithm and how it was applied.

5.	Fixed all bugs within the code.

6.	Added other paths to find out if the algorithm works.

7.	Did understand how the problem was solved but like I mentioned, it was challenging. 
