class Solution:
    def __init__(self):
        self.result = []

    def getPermute(self, cur_permute: List[int], next_nums: List[int]) -> List[int]:
        """
        My Solution:

        Recursion, Back Tracking

        logic:
            - each number in array as leaf in the level of tree
            - in each level
                - put current number in to current permute
                - remove this number in the nums
                - jump to next level

        time  O(10^N)
        space O(M^N)

        """
        if len(next_nums) == 0:
            self.result.append(cur_permute)
        for i in next_nums:
            t = next_nums[:]
            t.remove(i)
            self.getPermute(cur_permute + [i], t)

    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums:
            self.getPermute([], nums)
        return self.result
