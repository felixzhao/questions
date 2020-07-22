# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def find(self, root: TreeNode, path: str) -> None:
        """
        My Solution (Accepted)
        Recursive

        logic:
        - add a parameter 'path' to save the path from root to leafs
        - init with root val
        - in each level add current val to path
        - add to res when reach leaf

        time  O(N)
        space O(N)

        """
        if not root:
            return
        if not root.left and not root.right:
            self.res.append(path)
        if root.left:
            self.find(root.left, f'{path}->{root.left.val}')
        if root.right:
            self.find(root.right, f'{path}->{root.right.val}')

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.find(root, f"{root.val}")
        return self.res

    def binaryTreePathsIterations(self, root: TreeNode) -> List[str]:
        """
        Iterations
        (queue FILO or stack FIFO)

        logic
        - init root as node and root.val as path in queue
        - add to res when reach leaf
        - add left and right to queue, if existed

        time  O(N)
        space O(N)
        """
        if not root:
            return []
        res = []
        queue = [(root, f'{root.val}')]
        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                queue.append((node.left, f'{path}->{node.left.val}'))
            if node.right:
                queue.append((node.right, f'{path}->{node.right.val}'))
        return res

