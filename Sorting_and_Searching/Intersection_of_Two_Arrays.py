class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        My Solution

        Set Intersection

        logic
            - transfter array to set
            - call python function to do the intersection

        time  O(S + T + S + T) = O(N), S len(num1),T len(num2), set() O(1), .interestion O(S + T)
        space O(1 + S*T) = O(N^2), set() O(1) + .intersection worse case O(S*T)

        reference:
            - python operation complexity
              https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt

        """
        return set(nums1).intersection(set(nums2))
