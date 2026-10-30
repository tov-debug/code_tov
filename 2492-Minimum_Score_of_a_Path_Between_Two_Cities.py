"""
Problem Summery: Given n cities connected by two-way roads with distances, the path score is the length of its shortest road.
    We have to find the lowest possible path score between city 1 and city n, where you can use the same roads and cities again, 
    and we guaranteed that there is at least one.

Approch: Knowing we can use the same road multiple times, and the fact that the score only impact by the lowest road in the path-
    the question is to find the minimum distance btween two nodes in the given graph(we are uaranteed that there is at least one path).
    So simple building of the graph and looking for the minumum distance.
"""
#Using DFS.
#Time Complexity: O(|V||E|) - when V & E are the nodes and edges of the graph, visit at most 2 times each edge and one time each node.
#Space Coplexity:O(|V|+|E|) - for holding the garph and the visited list.
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        min_distance = 10**4

        #building the graph
        graph = {i: [] for i in range(1, n+1)}
        for road in roads:
            nodeA,nodeB,distance = road
            graph[nodeA].append((nodeB,distance))
            graph[nodeB].append((nodeA,distance))
        
        visited = []#for kepping track of visits
        queue = deque()
        queue.append(1) #there is must to be a way from 1 to n
        while queue:
            curr = queue.popleft()

            #looping over all curr neigbers to look for min distance
            for node,dis in graph[curr]:
                min_distance = min(min_distance, dis)

                if node not in visited:
                    visited.append(node)
                    queue.append(node)
        
        return min_distance


#you can also use another search to the min distance, for exmple: DFS with a stack instead of the queue(or simple requrtion with memoiazion)



        