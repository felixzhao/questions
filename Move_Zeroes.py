class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Simple Way

        time  O(N)
        space O(N)

        logic
            - push all non-zero into a queue, count non-zero at same time
            - pop queue into the result
            - set rest of others to zero
        """
        q = []
        no_zero_count = 0
        for n in nums:
            if n != 0:
                q.append(n)
                no_zero_count += 1
        for i in range(len(q)):
            nums[i] = q.pop(0)
        for i in range(no_zero_count, len(nums)):
            nums[i] = 0
