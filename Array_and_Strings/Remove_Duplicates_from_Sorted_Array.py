class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        time  O(N)
        space O(1)
        
        key point: 
        - the elements in list must move to non duplicate (begining part)
        - e.g. [1,1,2,2,2,3,3] => [1,2,3,2,2,3,3]
        """
        if len(nums) < 2:
            return len(nums)
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count
