Perfect Squares

1.	The problem is to find the least number of perfect square number from a given integer. The recursive equation used to solve this problem is:
dp[i] = min(dp[i], dp[i – k * k] + 1)
This  will get the minimum from the value in the list and the perfect square value. This will be counted and the last value of the created list will be the number of the total number of perfect squares.

2.	Since we are getting the total number of the perfect squares, one must first get how many perfect squares can be added to equal a positive integer n. A list is used in conjunction to the recursive equation to check the number that falls under these parameters. The list is 1D to store the values and can be used for any given positive integer.

3.	IDEAL

I – Identify

The problem was to have an algorithm that provides the counts of the perfect squares and that the perfect squares can be summed up to the n number.  Storing the results in the list will help with not repeating additions that are less than n again. 

D – Define

The cause for this problem is that the perfect squares need to be summed up to a number n and count these perfect squares.

E – Explore

The best strategy here is to implement an algorithm than can check if a perfect square is less than n and then add another perfect square while making sure that they are counted. 

A – Act

Two loops will be used to check for all perfect squares that are less than n and another to be able to traverse all possible solutions so that the perfect squares can be combined and added. 

L – Learn

The outcome of this solution is interesting since in the selection of loops was different from previous problems. This helped to make sure the scope of the problem was resolved in conjunction with the traversal of the solution.  

Duke’s 7 steps

1.	First, I decided to write down some pseudo code by hand to get an idea of the general solution to the problem. This helped me to be able to come up with a rough algorithm to the solution of the problem.

2.	I worked the same problem that was in the example and worked backwards since I already knew the result.

3.	The pattern than I was able to see was that at a minimum a perfect square added with another perfect square had to be less than or equal to n, starting from 1^2, 2^2... k^2. 

4.	Since I worked backwards to find the solution to this problem I was tracing it from bottom to top and was able to trace back from top to bottom to make sure it all fit together. 

5.	I now translated the pseudo code to actual python 3 code and fixed minor problems.

6.	After I managed to get the desired result, I added different test cases and check if the result was correct.

7.	From there all bugs, mostly syntax, were fixed.
