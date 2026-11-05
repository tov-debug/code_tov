"""
Problem Summery: for a given mXn grid we have to return True if possible to go from (0,0) cell to 
(m-1, n-1) cell with health heiger than 1, cell with '1 value reduce health by 1.

Approch: simple searching for a safe path while mainting the health by visits.
"""
#DFS + memo + backtrack
#Time Complexity: O(M*N*health) - all posible state computed once.
#Space Complexity: O(M*N*health) - for the recursion stack.
class Solution1:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        visited = set()#to avoid cycles
        memo = {}#to avoid duplicate calculation
        def dfs(i,j, health):
            if i >=len(grid) or i < 0 or j <0 or j >= len(grid[0]):#edge case
                return False

            health -= grid[i][j]
            if health <=0:#run out of health
                return False

            if (i,j,health) in visited:#didnt manage to get out
                return False 
            
            if (i,j,health) in memo:#this state been caluculated
                return memo[(i,j,health)]

            if i == len(grid) -1 and j == len(grid[0]) -1:#found path
                return True

            visited.add((i,j,health))#mark the begining of a run

            #all posibole moves:
            up = dfs(i-1,j,health)
            down = dfs(i+1, j, health)
            right = dfs(i, j+1, health)
            left = dfs(i, j-1, health)

            memo[(i,j,health)] = up or down or right or left
            
            if memo[(i,j,health)]:
                return True

            visited.remove((i,j,health))#backtracking
            return False

        return dfs(0,0,health)



# # # # # # # # # # # # # # # # # # # # # 

#BFS + priority to '0' cells
#Time Complexity: O(M*N) - each cell is only updated limited number of times before no better health remains.
#Space Complexity: O(M*N) - for queue.
class Solution2:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
       
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        queue = deque()
        queue.append((0, 0, health - grid[0][0]))#statrting from (0,0)
        while queue:
            r, c, health = queue.popleft()

            if r == len(grid) - 1 and c == len(grid[0]) - 1 and health > 0:#finish safty
                return True
            
            if (r, c) in visited or health <= 0: #not a path
                continue

            visited.add((r, c))#mark this cell as visited

            #all posibole moves:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and  (nr, nc) not in visited:#possible path
                    if grid[nr][nc] == 0:
                        queue.appendleft((nr, nc, health - grid[nr][nc]))#to check immeditly

                    else:
                        queue.append((nr, nc, health - grid[nr][nc]))#for later

        return False
     
 


    