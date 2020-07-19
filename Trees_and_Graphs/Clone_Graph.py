"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        """
        DFS

        logic:
            - keep a visited dictionary
                - key is original node, value is the clone node
            - if None or visited return from visited dictionary
            - otherwise, recursive all neighbors for original node

        key points:
            - in Clone Node initial neighbors as empty list []

        time  O(N)
        space O(N)
        """
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        cloneNode = Node(node.val, [])
        self.visited[node] = cloneNode
        if node.neighbors:
            cloneNode.neighbors = [self.cloneGraphDFS(n) for n in node.neighbors]
        return cloneNode


    def cloneGraphBFS(self, node: 'Node') -> 'Node':
        """
        BFS
        (queue + visited dictionary)

        logic
            - basic idea
                - visited dictory, keep processd node and clone node pair
                - queue (FIFO), keep neighbors
                - visited list as the result
            - process
                - init queue with root
                - until queue empty do
                - pop node, process all neighbors

        key points:
            - clone node with empty list as the init neighbors
            - clone when node not in visited
            - exponse neighbers in loop

        time  O(N)
        space O(N)
        """
        if not node:
            return node
        visited = {}
        queue = []
        queue.append(node)
        visited[node] = Node(node.val, [])
        while queue:
            cur = queue.pop(0)
            for n in cur.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    queue.append(n)
                visited[cur].neighbors.append(visited[n])
        return visited[node]


