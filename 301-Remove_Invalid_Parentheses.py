"""
Problem Summary:
Removes the minimum number of invalid parentheses to make the input string valid.
        
Approach:
1. Calculate the total minimum deletions needed.
2. Use backtracking to generate all valid combinations with exactly that number of deletions.
"""

# Try all keep/remove choices up to 'delete' limit, collect valid results in a set.
# Time Complexity:  O(2^N) - worst-case 
# Space Complexity: O(N)-  recursion depth.
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        open, close = 0,0
        #calculate total minimum removals needed
        for ch in s:
            if ch == '(':
                open += 1
            elif ch == ')':
                if open > 0:
                    open -= 1
                else:
                    close += 1
        delete = close + open

        # checks if a string has balanced parentheses
        def is_valid(st):
            open = 0
            for ch in st:
                if ch == '(':
                    open += 1
                elif ch == ')':
                    open -= 1
                if open < 0:
                    return False
            return open == 0

        ans = set()
        def req(i, st,delete):
            if i == len(s):#reached the end of the string
                if delete == 0 and is_valid(st):
                    ans.add(st)
                return

            if delete > 0 and (s[i] == '(' or s[i] == ')'):#remove current character
                req(i+1, st, delete-1)

            #keep current character
            req(i+1, st + s[i], delete)
        
        req(0,"", delete)
        
        return list(ans)