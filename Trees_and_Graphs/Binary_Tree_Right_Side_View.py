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
        return

        def rightSideView(self, root: TreeNode) -> List[int]:
            """
            Good Approach

            Queue
            (one queue + level length measurements)

            logic
                - init queue with root
                - in loop
                    - get length of queue length
                    - pop node in queue with the length
                    - only add length - 1 node into res

            time  O(N)
            space O(N), D is max width of tree, worse case N/2 (complete tree)
            """
            if not root:
                return []
            res = []
            queue = [root]
            while queue:
                length = len(queue)
                for i in range(length):
                    node = queue.pop(0)
                    if i == length - 1:
                        res.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return res

    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        DIRECTLY COPY ANSWER
        (because of it trick)

        DFS
        Recursive

        Trick Approach

        logic:
            - recursive
            - only level == len(res), then put to res
            - loop child right first

        time  O(N)
        space O(N), N=H is the hight of tree

        """
        if root is None:
            return []

        rightside = []

        def helper(node: TreeNode, level: int) -> None:
            print(f'rightside {rightside}')
            print(f'level {level}, len {len(rightside)}, node {node}')
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:  # key point, put right at first
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside