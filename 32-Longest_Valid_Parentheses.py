"""
Problem Summary:
Find the length of the longest valid parentheses substring.

Approach:
Use a stack to store indices, For '(' push current index, For ')' pop top index.
Case the stack becomes empty- push current index as the new base boundary.
Case stack is not empty- update max length.
"""
# Time Complexity: O(N) - single pass over string s.
# Space Complexity: O(N) - stack stores indices up to length N.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mx = 0
        st = [-1] #base boundary index

        for i, chr in enumerate(s):
            if chr == '(':
                st.append(i)
            else:
                st.pop()
                
                if not st:
                # the urrent ')' has no matching '(' 
                    st.append(i)
                else:
                    #  valid substring start from stack[-1] to i
                    mx = max(mx, i - st[-1])

                    
        return mx

        