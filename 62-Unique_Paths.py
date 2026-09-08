"""
Problem Summary:
Given an mxn grid, find the number of possible unique paths from the top-left corner 
to the bottom-right corner. moves only allowd down or right.

Approach:
Think of this as a grid where each cell stores the number of ways to reach the finish.
Since we can only move down or right, the number of paths from any current cell is simply 
the sum of the paths from the cell directly below it and the cell directly to its right.
"""


# 2D Bottom-Up Matrix
# Time Complexity: O(M * N) - Fills an (M+1) x (N+1) grid using nested loops.
# Space Complexity: O(M * N) - Stores the full 2D matrix in memory.
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize the grid with extra row & col of zeros
        dp = [[0]* (n+1) for _ in range(m+1)]
        dp[m][n-1] = 1 #the end
      
        # loop backwards from the destination towards the start
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]= dp[i][j+1] + dp[i+1][j]#right + down
        return dp[0][0]
      
# # # # # # # # # # # # # # # # # # # 


# 1D Space-Optimized DP (Row-by-Row)
# Time Complexity: O(M * N) - Same total iterations as 2D DP.
# Space Complexity: O(N) - Keeps only two 1D rows of size N.
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # represents the bottom row (only 1 way to reach the end -by going right)
        dp = [1] * n

        # loop for the remaining rows moving upwards
        for i in range(m-1):
            next = [1] * n #represent the next row
            # loop columns right to left, without the last col
            for j in range(n-2, -1, -1):
                next[j] = next[j+1] + dp[j] #right + down 
            dp = next
          
        return dp[0]

        
