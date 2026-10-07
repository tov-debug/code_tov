"""
Problem Summary:
For a given balanced parentheses strings we return the score of the string as follow:
when it full wraped multipie the part inside otherwise adding  the two parts.

Approach:
First for each index we will find his maching parenthes using a stack.
When we have the closer for each open (, we can check if it a multipie case or adding and sending it to the requrtion.
"""
# Divide and conquer - using indices lookup for fast splitting.
# Time Complexity: O(N) - O(N) to map indices plus O(N) total across all recursive calls since each step takes O(1).
# Space Complexity: O(N) - For storing the stack&dictionary and the recursion call stack.
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        #first for each index we will find his maching parenthes
        stack = []
        indexes = {}
        for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:# char is )
                indexes[stack.pop()] = i
        
        def req(right:int, left:int)->int:
            if right == left+1:#simple ()
                return 1
            if right <= left:#edge case
                return 0

            curr_right = indexes[left]
            if curr_right == right:#full wrap
                return 2* req(right-1, left+1)

            #two parts:
            return req(curr_right,left) +  req(right, curr_right+1)

        return req(len(s)-1,0)
            