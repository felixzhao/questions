class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        - sort nums at first
        - go through item in nums, without last two (because, three sum)
        - after first item skip duplicates
        - after item i, set l,r as begin, end of flowing sub string
        - sum three items
        - if larger l move to right
        - if small r move to left
        - if math, add to res, move l, r skip duplicate items
        
        time O(nlogn +n^2) = O(n^2) 
        space O(1)
        """
        res = []
        nums.sort()
        print(nums)
        target = 0
        for i in range(len(nums) - 2):
            print('i ' + str(i))
            if i > 0 and  nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                n = nums[i] + nums[l] + nums[r]
                print('n ' + str(n))
                if n < target:
                    l += 1
                elif n > target:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l<r and  nums[l] == nums[l + 1]:
                        l += 1
                    while l<r and nums[r] == nums[r - 1]: # 
                        r -= 1
                    l += 1 # move if equal, other condition already moved
                    r -= 1 # move if equal, other condition already moved
        return res
        
