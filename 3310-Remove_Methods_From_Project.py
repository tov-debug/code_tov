"""
Problem Summary:
Find all nodes infected by node k.
A node is infected if it is the starting node k, or if it can be reached from k through a chain of connections.
If any healthy node points to an infected one, return all nodes. Otherwise, return only the healthy nodes.

Approach:
Think of this as a network of sick and healthy nodes. 
We want to remove all the sick ones (if there is no healthy one pointing at one of the sick nodes we found).
We build a simple graph and use a stack to spread from k to all sick nodes. 
Finally, we check if a healthy node points to a sick one- if so, we keep all nodes, otherwise we remove the sick ones.
"""


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        sick = {k} #for keeping the sick nodes
        stack = [k] #to move for one neighbor to another 
        ans = range(n)# all the nodes

        # build the graph
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
          
        # find all sick nodes
        while stack:
            curr = stack.pop()
            for node in graph[curr]:
                if node not in sick:
                    stack.append(node)
                    sick.add(node)

        # check if there is no healthy pointing on sick
        for pair in invocations:
            if (pair[0] not in sick) and (pair[1] in sick):
                return list(ans) #the whole list of node
              
        # the final list     
        return [x for x in range(n) if x not in sick]
