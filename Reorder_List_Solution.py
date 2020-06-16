# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        1->2->3->4
        len(arr)/2 = 4/2 = 2
        arr = [1->4, 2->3, 3->^, 4->2]
        
        1->2->3->4->5
        len(arr)/2 = 5/2 = 2
        arr = [1->5, 2->4, 3->^, 4->3, 5->2]
        
        time  O(N)
        space O(1)
        
        """
        if not head:
            return head
        arr = []
        p = head
        while p:
            arr.append(p)
            p = p.next
        for i in range(int(len(arr) / 2)):
            arr[i].next = arr[-(i+1)]
            arr[-(i+1)].next = arr[i+1]
        arr[int(len(arr) / 2)].next = None
        
        
