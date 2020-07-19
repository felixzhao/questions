# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        My Solution

        Recursive

        logic
            - recursive left and right branch
            - if reach empty leaf return
            - put processed left branch to root.right
            - find the end of the processed left branch, put processed right branch follow it.

        Key Points
            - original left branch Must set to None

        time  O(N), as we process each of the node
        space O(N), the worse case all node in left branch, so the size of recursive stack is N.

        """
        if not root:
            return None
        l = self.flatten(root.left)
        r = self.flatten(root.right)
        root.left = None
        p = root
        if l:
            root.right = l
            p = l
            while p.right:
                p = p.right
        if r:
            p.right = r
        return root

