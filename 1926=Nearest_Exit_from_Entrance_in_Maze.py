"""
Problem Summery: for a given entarance coordinate at a grid, when '.' represent a empty cell and '+' represent a wall.
    We will return the minimum steps in the way out of the grid trow empty cells, and -1 if there is no such path.

Approch:  mark the starting point in 0 and spreding around to possible neigbers while marking each cell with +1,
finnaly the first exit we found wil have the privious position's value as the number of minimum step.
"""
#BFS + visited to avoid multi visits
#Time Comlexity: O(N*M) - the size of the grid, visiting each cell at most once.
#Space Comlexity: O(M*N) - for holding the queue and visited that will hold at most all cells.
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        visited = set()#for marking each visited cell
        dir = [(1,0), (0,1), (-1,0) , (0,-1)]

        maze[entrance[0]][entrance[1]] = 0#beggining

        queue.append(entrance)
        while queue:
            r,c = queue.popleft()
            if (r == len(maze)-1 or c == len(maze[0])-1 or r == 0 or c== 0) and ([r,c] != entrance):#made it to the edges of the maze but not entarance.
                    return maze[r][c] #holding the step

            #looping in all possible direction
            for dr,dc in dir:
                row,col = r + dr, c+dc
                
                if row >= len(maze) or row < 0  or col >= len(maze[0]) or col < 0  or maze[row][col] == '+' or (row,col) in visited:#skip
                    continue
                
                visited.add((row,col))#mark as visited
                maze[row][col] = maze[r][c] + 1#adding one step to next round
                queue.append([row,col])#moving on
            
        return -1#didnt find path


  #you can also use another search to the near enternce, for exmple: DFS with a stack instead of the queue(or simple requrtion with memoiazion)
      