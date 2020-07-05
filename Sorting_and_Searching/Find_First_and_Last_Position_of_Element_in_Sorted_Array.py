class Solution:
    def search_fist_or_last_match(self, nums: List[int], target: int, is_left: bool) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target or (is_left and nums[mid] == target):
                r = mid
            else:
                l = mid + 1
        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_match = self.search_fist_or_last_match(nums, target, True)
        if first_match == len(nums) or nums[first_match] != target:
            return [-1, -1]
        return [first_match, first_match + self.search_fist_or_last_match(nums[first_match:], target, False) - 1]
