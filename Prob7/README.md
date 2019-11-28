Integer Break

1.	This problem consists of receiving any positive integer and then breaking it into the sum of at least two digits and maximizing the product of the integers. For the recursive equation, we get:
dp[i] = max(max(dp[i], i) * max(dp[j],j), dp(i + j])
So this gets the numbers that if two digits added are less than or equal to whatever integer is received, if it is then it’s given to this equation where it is maximized and added to a list. Once all possibilities are tried, whichever value is stored in the list at the position of the number that was given is stored. 

2.	This problem was really interesting due to how it squares the results that are less than the given number. Each number that fits the constraints mentioned above is then stored and then multiplied with the other stored results to get the result. The best way to store the result is a 1D list. I tried a 2D list but found that storing and then multiplying the result in the same list to be the best solution.

3.	IDEAL

I – Identify

The problem is to break down the given number with integers that if added add back to the given number. Then instead of adding the numbers one must multiply these numbers to the max product. 

D – Define

Break the number into parts that if added make the given number. Then store the result of multiplying these numbers and return that result.

E – Explore

The algorithm for this problem was very interesting since it is storing the multiplication of the product and two for loops are used along with an if statement to make sure the numbers that are broken down are less than or equal to the given number.

A – Act

The parameters used in the for loops are used based on the abstraction of the problem.

L – Learn

I learned a lot from this problem do to the algorithm used.

Duke’s 7 steps

1.	Pseudo code was used to based on steps on how I thought the problem needed to be solved.

2.	Based on the examples provided I worked from top to bottom since I was able to identify the steps needed to come up with the solution.

3.	The pattern identified was that every integer checked must be less than n and when there is more than 1 it may be equal to n when added.

4.	Tracing the algorithm attempted helped me get more abstract details that were ignored.

5.	Translated the problem into actual code with minimum effort.

6.	Tried other numbers to see if the algorithm worked.

7.	Got mostly syntax errors and managed them.

