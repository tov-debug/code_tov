"""
Problen summary: calculate the n number in fibonacci series.
    fibonachi series defiend as folow-
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

Approch: acoording to the series definition we will calculate by using each time the 2 previus numbers.
"""

#Top-down dp, using dfs + memoization
#Time Complexity: O(n)- Each subproblem is computed once and stored in O(1) time, for n broblems at most.
#Space Complexity: O(n)- Requires space for the memo table and the call stack.
class Solution1:
    def fib(self, n: int) -> int:
        memo = {}
        def req(n):
            if n == 0 or n == 1:#base case
                return n
            if n in memo:#already calculatade 
                return memo[n]
            num1, num2 = req(n-1),req(n-2)#the pre nums
            memo[n] = num1 + num2
            return memo[n]
        return req(n)

#Buttom-up dp, looping over from zero to N keeping 2 numbers each time.
#Time Complexity: O(n)- Looping from 0 to n.
#Space Complexity: O(1)- Only the 2 numbers are kept.
class Solution:
    def fib(self, n: int) -> int:
        num1,num2 = 0,1

        for _ in range(n):
            num1,num2 = num2, num1+num2

        return num1


        
    