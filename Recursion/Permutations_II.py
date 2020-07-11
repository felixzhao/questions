class Solution:
    def __init__(self):
        self.result = []

    def backtrack(self, permute: List[int], nums: List[int]) -> None:
        """
        My Solution

        Recursion, Backtrack

        logic:
            - similar with Question "Permutations"
            - each number in nums as a element in a level in the tree
            - in each level skip the duplicate number
            - jump to next level without the number
            - when nums empty, put into result

        python:
            - deep copy
                new_arr = arr[:]
            - list to set
                s = set(l)

        time  O(10^M), M not include the duplicate numbers
        space O(10^M)

        """
        if len(nums) == 0:
            self.result.append(permute)
        for i in set(nums):
            t = nums[:]
            t.remove(i)
            self.backtrack(permute + [i], t)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums:
            self.backtrack([], nums)
        return self.result
