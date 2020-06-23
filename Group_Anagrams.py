class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        time  O(N)
        space O(N)
        
        - use sorted str as key save in dict, value is a list for all str with same chars
        - key point: 
          - string can not use .sort() in python, must use sorted()
          - list or set can not use as key in dictionary in python, so need trans back to string
        
        """
        res = []
        dit = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in dit:
                dit[ss] = []
            dit[ss].append(s)
        for k,v in dit.items():
            res.append(v)
        return res
