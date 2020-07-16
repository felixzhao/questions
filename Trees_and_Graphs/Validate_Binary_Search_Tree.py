# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isValidated = True

    def check(self, root: TreeNode) -> (int, int):
        """
        My Solution

        logic:
            - get low from left branch
            - get high from right branch
            - if root <= left low, set global value to False
            - if root >= right high, set Flase

        time  O(N)
        space O(N)

        """
        low, high = root.val, root.val
        if root.left:
            l, h = self.check(root.left)
            if h >= root.val:
                self.isValidated = False
            low = l
        if root.right:
            l, h = self.check(root.right)
            if l <= root.val:
                self.isValidated = False
            high = h
        return low, high

    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            self.check(root)
        return self.isValidated
