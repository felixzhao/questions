# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float(-inf)

    def getMaxPathSum(self, node):
        """
        Recursive

        Good Question
            - DONT think it too complex

        logic:
            - keep a global value to save the value of max sum
            - recursive condition, empty leaf return 0
            - inner sum = l + r + val, if larger than max_sum, then update it
            - return outer sum = max(l, r) + val to parent level

        Key Points
            - l or r get val or 0, if val < 0
                - this code is works for skip uncontine max
            - boundary cases:
                - [-3] only negative value
                - [1, -1, 3] uncontine max

        time  O(N)
        space O(logN)

        """
        if not node:
            return 0
        l = max(self.getMaxPathSum(node.left), 0)
        r = max(self.getMaxPathSum(node.right), 0)
        current = l + r + node.val
        self.max_sum = max(self.max_sum, current)
        return max(l, r) + node.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.getMaxPathSum(root)
        return self.max_sum
