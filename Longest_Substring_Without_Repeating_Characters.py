class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        j = 0
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                j = max(j, dic[s[i]] + 1)
            dic[s[i]] = i
            res = max(res, i-j+1)
        return res
