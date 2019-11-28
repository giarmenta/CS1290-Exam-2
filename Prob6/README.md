Maximum Length of Pair Chain

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
