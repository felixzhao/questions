import math
INT_MAX = 2147483647
INT_MIN = -2147483648


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        check i out of len(s) is needed in each loop
        key method: total = total * 10 + digital
        """
        if len(s) == 0:
            return 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                break
        sign = 1
        if i < len(s):
            if s[i] in ['+', '-']:
                if s[i] == '-':
                    sign = -1
                i += 1
        total = 0
        while i < len(s):
            if (ord(s[i]) < ord('0')) or (ord(s[i]) > ord('9')):
                break
            digital = ord(s[i]) - ord('0')
            total = total * 10 + digital
            i += 1
        total *= sign
        return max(INT_MIN, min(total, INT_MAX))
