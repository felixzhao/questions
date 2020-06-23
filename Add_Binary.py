class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        time == space O(max(M,N))
        
        key points
        - fill zero at left
        - go trough from right to left
        - only sum '1' 
        - add '1' to answer if odd, otherwise add '0' ( by % 2)
        - get next carry by // 2
        - reverse res
        """
        res = []
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        carry = 0
        for i in range(len(a)-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                res.append('1')
            else:
                res.append('0')
            carry //= 2
        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)
