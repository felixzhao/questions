# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 1

    def find(self, root: TreeNode) -> int:
        """
        tricky question
        Recursive
        (you know it if you known it, just remember it)

        logic:
        - keep global answer
        - recursive left and right
        - keep ans with the max subtree
        - return max left or right branch + current node to parent
        - minus one at top level, as root node not include in the length

        time  O(N)
        space O(N)
        """
        if not root:
            return 0
        l = self.find(root.left)
        r = self.find(root.right)
        self.ans = max(self.ans, l + r + 1)
        return max(l, r) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.find(root)
        return self.ans - 1
