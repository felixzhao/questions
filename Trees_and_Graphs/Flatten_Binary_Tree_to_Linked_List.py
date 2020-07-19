# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Good Question
    """
    def flattenRecursive(self, root: TreeNode) -> None:
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
        l = self.Recursiveflatten(root.left)
        r = self.Recursiveflatten(root.right)
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

    def flattenMorrisTravelsal(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        Good Solution

        Morris Travelsal (Inorder Travelsal)
        https://www.educative.io/edpresso/what-is-morris-traversal
            - useful
            - hard to understand

        logic:
            - find the right most of left branch
            - put original right branch folowing the left- right most node
            - move current left to right
            - until right is None

        Key Points:
            - after put original right branch to left-rightmost node
                - must move current left node to right
                    - node.right = node.left
                - must clean up left node
                    - node.left = None


        time  O(N)
        space O(1) ??? why it's O(1), I think it less than recursive solution, but still O(N), not quite sure.

        """
        if not root:
            return None
        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
