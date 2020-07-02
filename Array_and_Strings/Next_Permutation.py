class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        time  O(N)
        space O(1)
        
        3 key points:
        1. if orignal desc sort, reverse list
        2. otherwise, from right to left find first (left > right) => arr[i]
        3. after that, from right to left find first lager than that (arr[j] > arr[i])
        4. (important) reverse list after i
        
        related resource:
        Permutation: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
        """
        if len(nums) < 2:
            return nums
        i = len(nums) - 2
        while i >= 0:
            if nums[i+1] > nums[i]:
                break
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j > i:
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
                j -= 1
        self.reverse(nums, i + 1)
        
    def reverse(self, nums: List[int], start: int) -> None:
        if start >= len(nums): return
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
        
