"""
Problem Summary:
Given 2 strings, return the length of their longest common subsequence.
Sunsequence- a sequence that foremd from another sequence, by deleting some or no elements 
  without changing the order of the string.

Approach:
Think of this as a grid, where one string sits on top and the other sits on the side.
Each call at the grid checks the match between two characters:
- Match: Add 1 to the diagonal cell(to continue with the score before those two character).
- Mismatch: Take the max from adjacent cells(right or down), which represent skipping one character in one of the strings.

Start with top-down memoization, move to a 2D grid, and finally optimize space down to 1D.
"""

# Top-Down Recursion with Memoization
# Time Complexity: O(M * N) - Each unique state (i, j) is calculated once.
# Space Complexity: O(M * N) - Memoization table storage + recursion stack depth of O(M + N)
class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
      
        def req(i:int, j:int)->int:
            if i == len(text1) or j == len(text2): #stopping condition
                return 0
            if (i,j) in cache: #already been calculate
                return cache[(i, j)]
            if text1[i] == text2[j]: #match
                cache[(i, j)] = 1 + req(i+1, j+1)#keeping this pass
            else: #mismatch
                cache[(i,j)] = max(req(i,j+1), req(i+1, j))#trying to skip one character
            return cache[(i,j)]
          
        return req(0,0)
      
# # # # # # # # # # # # # # # # # # # #     


# 2D Bottom-Up Matrix
# Time Complexity: O(M * N) - Fills an (M+1) x (N+1) grid using nested loops.
# Space Complexity: O(M * N) - Stores the full 2D matrix in memory.
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # initialize the grid with extra row&col of zeros for base case
        dp = [[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]
      
        #loop from the end of both strings towards the start
        for i in range(len(text2)-1, -1, -1):
            for j in range(len(text1)-1, -1, -1):
                if text1[j] == text2[i]: #match
                    dp[i][j] = 1+ dp[i+1][j+1]#keeping this pass
                else: #mismatch
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) #trying to skip one character
                  
        return dp[0][0]
# # # # # # # # # # # # # # # # # # # #   

# 1D Space-Optimized DP (Row-by-Row)
# Time Complexity: O(M * N) - Same total iterations as 2D DP.
# Space Complexity: O(M) - Keeps only two 1D rows of size M + 1 (where M is length of text1).
class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # represents row i + 1 (initially the bottom padded row of zeroes)
        row = [0 for j in range(len(text1)+1)]
      
        #loop text2 botton to top
        for i in range(len(text2)-1, -1, -1):
            # temporary storage for current row i
            newRow = [0]* (len(text1)+1)
            # loop text1 right to left
            for j in range(len(text1)-1, -1, -1):
                if text1[j] == text2[i]: #match
                    newRow[j] = 1 + row[j+1] #keeping this pass
                else: #mismatch
                    newRow[j] = max(row[j], newRow[j+1]) #trying to skip one character
            row = newRow
          
        return row[0]
