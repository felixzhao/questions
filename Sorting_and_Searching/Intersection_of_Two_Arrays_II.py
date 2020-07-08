"""
What if the given array is already sorted? How would you optimize your algorithm?

We can use either intersectSort, dropping the sort of course. It will give us linear time and constant memory complexity.
What if nums1's size is small compared to nums2's size? Which algorithm is better?

intersect is a good choice here as we use a hash map for the smaller array.
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

If nums1 fits into the memory, we can use intersect to collect counts for nums1 into a hash map. Then, we can sequentially load and process nums2.

If neither of the arrays fit into the memory, we can apply some partial processing strategies:

Split the numeric range into subranges that fits into the memory. Modify intersect to collect counts only within a given subrange, and call the method multiple times (for each subrange).

Use an external sort for both arrays. Modify intersectSort to load and process arrays sequentially.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Hard Question, Smart Result

        Dictionary

        logic
            - a dictionary save the element and count in shorter list
            - check element longer list if existed in dictionary and count > 0, add to result(shorter list)
            - decrease count in dictionary

        key point
            - "Each element in the result should appear as many times as it shows in both arrays." means the count of both show element. e.g. [2,2], [2] => [2]
            - reuse shorter list as result list
            - thus, dictionary must generate from shorter list

        python tech:
            - best practice for get value from dictionary
              dic.get(key, 0)

        time  O(M + N)
        space O(min(M,N))

        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        dic = {}
        for i in nums1:
            dic[i] = dic.get(i, 0) + 1
        print(dic)
        j = 0
        for i in nums2:
            c = dic.get(i, 0)
            if c > 0:
                nums1[j] = i
                dic[i] -= 1
                j += 1
        return nums1[:j]

    def intersectSort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Sorting + pointers

        logic:
            - sort all list
            - 3 pointers for n1, n2 and res
            - loop compare n1, n2
                - move smaller side pointer
                - if equal set to result

        key points:
            - k start from 0, so after loop finish k = len(res) - 1. Thus, return nums1[:k]

        time  O(nlogn + mlogm)
        space O(1)

        """
        nums1.sort()
        nums2.sort()
        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
        return nums1[:k]