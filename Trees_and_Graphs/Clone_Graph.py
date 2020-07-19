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
