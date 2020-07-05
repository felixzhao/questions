class Solution:
    def romanToInt(self, s: str) -> int:
        """
        time  O(N)
        space O(1)
        
        specail case: IV <=> V - I <=> 5 - 1
        key point check two node with >=,
        do not forget ==
        
        algo:
        go through list for two node
        if first >= second, sum
        if first < second sub
        add up last node before return
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        value = 0
        for i in range(len(s) - 1):
            if dic[s[i]] >= dic[s[i+1]]:
                value += dic[s[i]]
            else:
                value -= dic[s[i]]
        return value + dic[s[-1]]
