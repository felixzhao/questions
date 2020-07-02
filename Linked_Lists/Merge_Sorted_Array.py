class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        time  O(M + N), M is |copy_num1| which is less then |nums1|
        space O(M)
        
        logic:
          - copy values from nums1
          - clean up nums1 may make logic simple
          - 2 pointers
            - compare and pick smaller into result
        
        key points
          - partial list copy is deep copy already, in python
        
        """
        copy_num1 = nums1[:m]
        i = 0
        j = 0
        k = 0
        while i < len(copy_num1) and j < len(nums2):
            if copy_num1[i] < nums2[j]:
                nums1[k] = copy_num1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < len(copy_num1):
            nums1[k] = copy_num1[i]
            k += 1
            i += 1
        while j < len(nums2):
            nums1[k] = nums2[j]
            k += 1
            j += 1
            
            
                
