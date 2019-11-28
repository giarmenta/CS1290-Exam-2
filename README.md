# CS1290-Exam-2
Exam 2 

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


2.  The Minimum Falling Path Sum 

1.	For this problem one must traverse the array of integers and add them. For example, when using a 3x3 square, one must add a digit from each row and get the lowest (minimum) sum as the answer with the constraint that it has to be at most 1 in difference.  The recursive function used is:
path = min(path, db[i + 1][j – 1])
path = min(path, db[i + 1][j +1])
This way the result is stored in the in the variable path. Once the variable is stored, this is stored in a 2D list and is added to the values of the list to get the sum of all possible paths. 
2.	The solution is stored in a 2D list as mentioned earlier. this is list is generated from traversing the 2nd and 3rd row with the test provided. The first row is stored for reference and form there all possible are checked with the constraint of each column have a difference of at most 1.
3.	IDEAL
4.	I – Identify
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


6.  Maximum Length of Pair Chain

1.	For this problem we are finding a chain in a 2D list where in every pair, the first number is smaller than the second number. To make a chain the second number from a pair has to be less than the first number of another pair. From there one must return the largest number of pair that can be formed. 
The recursive equation for this problem is:
dp[j] = max(dp[j], dp[i] + 1)
For this problem, the list will only append the values the meet the criteria of a pair’s second value being less than the first value of a pair. This needed to be repeated for all pairs to get the count.
2.	One must get the count of the total pairs that can be chained from the given list of pairs meeting the constraint of what makes a chain in this problem. Only two numbers are needed to be compared, one from each pair (the last and the first of the two pairs being compared). Two for loops can easily help with the traversal using the above algorithm. 
3.	IDEAL
I – Identify
The problem is to return the count of the chain that can be formed with the parameters mentioned that make up a chain. A chain can only be formed the second integer from the pair is less than the first integer from the other pair being compared. 
D – define
A chain consists of the integer at position [x][1] is less than the integer at position [2][y] making x and y irrelevant for this comparison since x will always be smaller than y.
E – Explore 
Since it is a chain that needs to be counted, the best solution is a list that can hold pairs. 
A – Act
I found this algorithm relatively easy by using identifying the abstract of the problem.
L – Learn
It made me realize that abstracting the problem can help a lot by identifying the solution.
Duke’s 7 steps
1.	Pseudo code was used to be able to come up with the solution to the problem.
2.	The count was the last thing that needed to be done but the chain needs to be stored in a list so that the total elements are returned.
3.	The pattern was easily recognized once the problem was abstracted and the important details were identified. 
4.	I managed to trace the problem back and forth to make sure that the algorithm made sense along with the traversal of each pair in the list.
5.	Minor bugs were fixed and easily identified.
6.	Made a list with different pairs to make sure that the algorithm worked.
7.	Minor syntax bugs were solved.


7. Integer Break

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
7.	Got mostly syntax errors and managed to fix them.


9. Perfect Squares

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
