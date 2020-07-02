"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
    """
    deep copy a linked list which have a random link to a node in this list
    """
        if not head:
            return None
        pre_header = Node(0)
        q = pre_header
        p = head
        old_node_arr = []
        new_node_arr = []
        while p:
            old_node_arr.append(p)
            q.next = Node(p.val)
            p = p.next
            q = q.next
        p = pre_header.next
        while p:
            new_node_arr.append(p)
            p = p.next
        for i in range(len(old_node_arr)):
            if old_node_arr[i].random:
                random_pos = old_node_arr.index(old_node_arr[i].random)
                new_node_arr[i].random = new_node_arr[random_pos]
            else:
                new_node_arr[i].random = None
        return new_node_arr[0]
