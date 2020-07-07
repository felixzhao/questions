class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        My Answer

        Sorting

        logic
            - generate a tuple array, save (value in ith place, number of ith place)
            - sort this array by first tuple value
            - return last tuple second tuple value

        time  O(NlogN)
        space O(2N) = O(N)

        """
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))
        arr.sort(key=lambda x: x[0])
        return arr[-1][1]

