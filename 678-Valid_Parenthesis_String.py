"""
Problem Summary:
Check if a string containing '(', ')', and '*' is valid, where '*' can act as '(', ')', or an empty string.

Approach:
Maintain current open parentheses count 'open' and index 'i', make sure it rached zero at the end -
which mean a valid parenthesis
"""
#Top-down dynamic programming (DFS + memoization)
# Time Complexity: O(N^2) - state space defined by i (up to N) and open count (up to N).
# Space Complexity: O(N^2) - memory used by memoization cache and call stack.
class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def dfs(open, i):
            if open < 0: # unmatched closing parenthesis
                return False

            if (open, i) in memo:#reached end of string
                return memo[(open, i)]

            if i == len(s):
                return open == 0

            if s[i] == '(':
                memo[(open, i)] = dfs(open+1,i+1)

            elif s[i] == ')':
                 memo[(open, i)] = dfs(open-1,i+1)

            else:#options for '*'
                memo[(open, i)] = dfs(open+1,i+1) or dfs(open-1,i+1) or dfs(open,i+1)

            return  memo[(open, i)] 

        return dfs(0,0)

        



#You can also solve this iteratively,using dp or a greedy approach.
#  which eliminates the recursion call stack entirely and optimizes the space complexity down to O(1).