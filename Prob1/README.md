1.	Stone Game

1.	For this problem one must either have Alex pick one value from either end of the array. This problem is similar to the house robbing problem which gives the following recursive equation: 
dp[i][i + d] = max(p[i] – dp[i + 1][i + d], p[i + d] – dp[i][i + d -1])
If Alex always goes first and gets the max value, he will always win. Based on the recursive equation, the first value is being compared with the second value with what has been obtained then gets the max value from those comparisons. This way the result is always being stored in a 2D array and even though one is only looking for if it will return true, one can also get the results if needed.

2.	The solution is stored in a 2D list that stores the results of each session of the game. Three for loops are used in order to traverse the list and do the comparisons necessary to store the results. In summary, a 2D list is created to store the values and regardless of what Lee plays, he will loose.

3.	IDEAL

I – Identify
The problem was not in getting the final result but deciding what algorithm to use if the results need to be stored. One is able to identify that Alex will always win but to store the results being that Alex picks first, then Lee.

D – Define

The problem is to get the result that each player gets stored and determining the winner of the game returning true if Alex wins.

E – Explore

The best strategy is to have a 2D list store the results the do comparisons getting the max value.

A – Act

Determining what logic to utilize was tricky considering that the comparisons must be made as well as traverse the list with the values representing the piles of stones.

L – Learn

Seeing this problem was similar to the house robber problem given in class which gave a good idea on how to apply the algorithm.

Duke’s 7 step

1.	Attempted to solve the problem with pseudo code to try to identify what algorithm was needed.

2.	Since the result was already known based on the assumptions listed, it was just a matter of identifying what algorithm to apply.

3.	This reminded me of the house robbing problem so I worked from there. It helped me to identify the patter where Alex will get all even.

4.	I traced the ¬¬¬pseudo code I did with how the problem was supposed to be solved, starting from what is needed to be done in steps which helped get the code done.

5.	Fixed minor syntax issues that came up when doing it in actual code.

6.	I added different number to the list to see if it works and it did.

7.	Did get many index out of bounds errors but managed.
