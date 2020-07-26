class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Dictionary

        logic:
        - keep a dictionary save 'target - nums[i]' as key, and i as value
        - if num in nums already existed in dictonary,
            which means we found the pair

        time  O(N)
        space O(N)
        """
        dit = {}
        for i in range(len(nums)):
            if nums[i] in dit:
                return [dit[nums[i]], i]
            else:
                dit[target - nums[i]] = i
