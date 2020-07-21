# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def find(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        """
        Recursive
        (Good and Clear Approach)

        logic:
        - keep 3 flags in each level
        - mid figure out current node match p or q
        - l, r figure out either left or right branch match p or q
        - if 2 of these 3 flags change to True, we found the result (lowest common ancestor)

        time  O(N)
        space O(N)
        """
        if not root:
            return False
        mid = False
        if root == p or root == q:
            mid = True
        l = self.find(root.left, p, q)
        r = self.find(root.right, p, q)
        if mid + l + r >= 2:
            self.ans = root
        return mid or l or r

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.find(root, p, q)
        return self.ans