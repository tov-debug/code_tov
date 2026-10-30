"""
Problem Summary:
For a given gtid containing islands that are represent as a group of positive cell.
We have yo return how many islands have sum that divided by K.

Approach:
We can travel over the grid cheking each non zero cell if can be a fitting island, marking the visits as sea(0).
"""

# DFS + memo.
# Time Complexity: O(M * N) - Each unique state (i, j) is calculated once.
# Space Complexity: O(M * N) - Memoization table storage + recursion stack depth of O(M * N)
class Solution1:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n,m = len(grid), len(grid[0])
        
        memo = {}
        def dfs(i,j):
            if i >= n or i < 0 or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            curr = grid[i][j]
            grid[i][j] = 0

            memo[(i,j)] = curr + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
            return memo[(i,j)]
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and dfs(i,j) % k == 0:
                    cnt += 1
        
        return cnt


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# BFS.
# Time Complexity: O(M * N) - visiting 
# Space Complexity: O(M * N) - Memoization table storage + recursion stack depth of O(M + N)
class Solution2:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        nei = [(0,1),(1,0),(0,-1),(-1,0)]
        n,m = len(grid), len(grid[0])
        cnt = 0

        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                
                sum = grid[i][j]
                grid[i][j] = 0
                queue.append((i,j))
            
                while queue:
                    row, col = queue.popleft()
                    for r,c in nei:
                        if r+row >= n or c+ col >= m or r+row< 0 or c+col < 0 or grid[r+row][c+ col] == 0:
                            continue
                        
                        sum += grid[r+row][c+ col]
                        grid[r+row][c+ col] = 0
                        queue.append((r+row,c+ col))
                
                if sum % k == 0:
                    cnt +=1 

        return cnt
        