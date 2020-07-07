class Solution:
    def findPeakElementSorting(self, nums: List[int]) -> int:
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

    def findPeakElementLinearScan(self, nums: List[int]) -> int:
        """
        Good Question

        Linear Scan

        logic:
            - following the question, we can return any peak as result
            - case 1: if each nums[i] > nums[i+1] then peak is the nums[0]
            - case 2: if each nums[i] < nums[i+1] then peak is the nums[-1]
            - case 3: if nums[i-1] < nums[i] > nums[i+1] then peak is the nums[i]
            - Thus, return the first element lager than the next
            - or if case 2 return last element

        time  O(N)
        space O(1)

        """
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    def findPeakElementRecursiveBinarySearch(self, nums: List[int]) -> int:
        return self.searchRecursiveBinarySearch(nums, 0, len(nums) - 1)

    def searchRecursiveBinarySearch(self, nums: List[int], l: int, r: int) -> int:
        """
        Good Question

        Recursive Binary Search

        logic:
            - start from mid
            - if mid > next
            - then search in left part
            - otherwise search in right part

        Key Points:
            - search left part, must l=l, r=mid (not mid+1)
            - because of we only compare mid and next of mid

        """
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            return self.searchRecursiveBinarySearch(nums, l, mid)
        return self.searchRecursiveBinarySearch(nums, mid + 1, r)

