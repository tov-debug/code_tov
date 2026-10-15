"""
Problem Summary:
Remove the outermost parentheses from every primitive valid parentheses string in 's'.

Approach:
Track the depth of parentheses using a counter - 
when it 0 it marks the outermost level of a primitive group.
"""
# Time Complexity: O(N) - single pass over the string.
# Space Complexity: O(N) - list used to construct the final string.
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        open = 0
        for ch in s:
            if ch == '(':
                if open != 0:
                    # state that it's inside an outer parenthesis.
                    res.append(ch)

                open += 1

            elif ch ==')':
                open -= 1

                if open != 0:
                    # state that it's not the outermost closing parenthesis.
                    res.append(ch)

        return "".join(res)

        