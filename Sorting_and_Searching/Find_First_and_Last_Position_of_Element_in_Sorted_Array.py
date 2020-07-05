class Solution:
    def search_fist_or_last_match(self, nums: List[int], target: int, is_left: bool) -> int:
        """

        key points:
            - this method is a little bit different with original binary search
            - as this need to fulfill with case nums:[8], t:8 and case nums:[8,8], t:8
            - so, r = len(nums) (not len(nums) - 1) and while l< r: (not l<=r)
            - actually,
                - when find first match, first mid is the one after original mid
                - when find last match, this algorithm is finding the element after last match

        """
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target or (is_left and nums[mid] == target):
                r = mid
            else:
                l = mid + 1
        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """

        Time  O(logN)
        Space O(1)

        logic:
            - two loop
                - first find the first match
                - second find the last match

        Attention:
            - the finding method is similar with original binary search but not fully same.

        """
        first_match = self.search_fist_or_last_match(nums, target, True)
        if first_match == len(nums) or nums[first_match] != target:
            return [-1, -1]
        return [first_match, first_match + self.search_fist_or_last_match(nums[first_match:], target, False) - 1]
