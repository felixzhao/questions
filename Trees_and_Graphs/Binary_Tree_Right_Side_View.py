# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        BFS
        Two Queues

        logic
            - BFS iterator each level
            - keep two queues to figure current level and next level
            - process
                - init root to next level queue
                - in loop move all elements from next level queue to current level queue
                - pop nodes in current queue, put left, right to next queue
                - when current queue empty, the last node poped is the rightmost element for this level

        time  O(N)
        space O(D), D=N/2 worse case complete tree, max node level count is N/2

        """
        if not root:
            return []
        res = []
        cur_q = []
        nex_q = []
        nex_q.append(root)
        while nex_q:
            cur_q = nex_q
            nex_q = []
            while cur_q:
                # print(f'cur_q {cur_q}')
                node = cur_q.pop(0)
                if node.left:
                    nex_q.append(node.left)
                if node.right:
                    nex_q.append(node.right)
            # print(f'node {node}')
            res.append(node.val)
        return res
