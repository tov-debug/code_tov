"""
Problem Summary:
Removes the minimum number of invalid parentheses to make the string valid.

Approach:
Mark invalid parentheses first, then build a new string without them.

"""
# Uses a stack to track indices of open parentheses '('.
# Time Complexity: O(N) - where N is the length of the string, just simple 2 pass over it.
# Space Complexity: O(N) - for the stack.
class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        s = list(s)
        stack = []

        for i in range(n):
            if s[i] == '(':
                stack.append(i)

            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:#a closer without an opener
                    s[i] = '-'

        #rest of openers that have no closer
        for i in stack:
            s[i] = '+'

        res = ""
        for ch in s:
            if ch == '+' or ch == '-':
                continue
            else:
                res += ch
        return res



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#To avoid use of stack with the same time&space complexity we can use counters.
#By keeping the result we immeditly delete with no need to mark and rebuilt.
class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        first_pass = []
        open = 0

        #lopping to delete invalid ')'
        for ch in s:
            if ch == '(':
                open += 1

            elif ch == ')':
                if open > 0:
                    open -= 1
                else: #invalid )
                    continue#skip it

            first_pass.append(ch)
        
        res = []
        close = 0
        #looping backwards on the first pass result to delete invalid '('
        for ch in reversed(first_pass):
            if ch == ')':
                close += 1

            elif ch == '(':
                if close > 0:
                    close -= 1
                else: #invalid (
                    continue#skip it
            res.append(ch)
        
        #reverse back to original order
        return "".join(reversed(res))
                

