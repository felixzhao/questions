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

    def moveZeroesV2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Smart Way

        time  O(N)
        space O(1)

        logic:
        (two pointers)
            - one pointer figure out last non zero position
            - another pointer figure out current position
        (two rounds)
            - first round, move all non zero to front
            - second round, set zero to follow up

        Analysis:
            - this method better than swap way,
                whatever lots of begining non-zero or zero
                this method only move when out of continue range
                because nums[1] = nums[1] will nothing happen

        """
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0