class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        sliding window approach
        https://medium.com/outco/how-to-solve-sliding-window-problems-28d67601a66
        
        time  O(S + T)
        space O(S + T)
        
        - 2 loops
          - out   loop r
          - inner loop l
        - fixed
          - w_dic    : map of char and count in window
          - expected : performed char in T
        - variable
          - t_dic    : map of char and count in T
          - actual   : how many unique char in T
        - result
          - ans saved in tuple
          - init with (inf, None, None)
        
        - python features
          - Inf                        : float('Inf')
          - "? :" expression in python : x if A == B else y
          
        - 2 bugs
          - inner loop check must use l <= r
            - the equal works for only one char in S and T
          - s[ans[1]: ans[2]+1], right side must add 1
            - otherwise will missing rightmost 
        
        """
        if not s or not t:
            return 0
        t_dic = {}
        for c in t:
            t_dic[c] = t_dic.get(c, 0) + 1
        # print(t_dic)
        expected = len(t_dic)
        w_dic = {}
        actual = 0
        l = r = 0
        ans = (float('Inf'), None, None)
        while r < len(s):
            c = s[r]
            w_dic[c] = w_dic.get(c, 0) + 1
            if c in t_dic and t_dic[c] == w_dic[c]:
                actual += 1
            # print(c)
            # print(w_dic)
            # print(actual)
            while l <= r and actual == expected: # l <= r, for only one char
                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r)
                c = s[l]
                w_dic[c] -= 1
                if c in t_dic and t_dic[c] > w_dic[c]:
                    actual -= 1
                l += 1
                # print(" >>> inner")
                # print(c)
                # print(w_dic)
                # print(actual)
                # print(ans)
                # print(" >>> inner end")
            r += 1
        return "" if ans[0] == float('Inf') else s[ans[1]: ans[2]+1] # right side must add 1
