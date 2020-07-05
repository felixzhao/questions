class Solution:
    def find_roation_start(self, left: int, right: int) -> int:
        nums = self._nums
        if nums[left] < nums[right]:
            return 0
        while left <= right:
            povit = (left + right) // 2
            if nums[povit] > nums[povit + 1]:
                return povit + 1
            else:
                if nums[left] < nums[povit]:
                    left = povit + 1
                else:
                    right = povit

    def binary_search(self, left: int, right: int, target: int) -> int:
        nums = self._nums
        while left <= right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            povit = (left + right) // 2
            if nums[povit] == target:
                return povit
            elif nums[povit] > target:
                right = povit - 1
            else:
                left = povit + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        """
        Good Question
        "Binary Search"

        Time  O(logN) => O(logN + logN)
        Space O(1)

        logic:
            - two process
                - 1. find start position of the sorted array (binary search)
                - 2. based on the start value and target compare result search target in left or right. (binary search)

        key points:
            - two split O(logN) process, cost O(logN) time complexity
            - no duplicate number in array is a constraint in question
        """
        self._nums = nums
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        # find rotation start
        rotation_start = self.find_roation_start(0, n - 1)
        print(rotation_start)

        if nums[rotation_start] == target:
            return rotation_start

        # if not rotation binary search
        if rotation_start == 0:
            return self.binary_search(0, n - 1, target)

        if nums[0] <= target:
            # search left
            return self.binary_search(0, rotation_start - 1, target)
        else:
            # search right
            return self.binary_search(rotation_start, n - 1, target)

