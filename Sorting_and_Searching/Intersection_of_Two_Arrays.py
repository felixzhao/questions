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

    def set_intersection(self, set1, set2) -> List[int]:
        return [x for x in set1 if x in set2]

    def intersectionTwoSet(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Two Set

        logic
            - Do Not use official implement intersection function
            - check element in set1 and set2

        key points
            - list comprehension with condition [x for x in A if C]

        Strange thing
            - use shorter length set at first take less time cost in list comprehension

        Time  O(M + N)
        Space O(M + N)
        """
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
    # test of call set_intersection vs short first
    #         start_time = time.time()
    #         res = self.set_intersection(set1, set2)
    #         print("--- %s seconds ---" % (time.time() - start_time))

    #         start_time = time.time()
    #         if len(set1) < len(set2):
    #             res = self.set_intersection(set1, set2)
    #         else:
    #             res = self.set_intersection(set2, set1)
    #         print("--- %s seconds ---" % (time.time() - start_time))
    #         return res
    # --- 2.384185791015625e-06 seconds ---
    # --- 1.430511474609375e-06 seconds ---
    # --- 9.5367431640625e-07 seconds ---
    # --- 1.1920928955078125e-06 seconds ---
