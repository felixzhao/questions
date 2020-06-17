class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        10, 3
        r = 3
        t = t
        10-3=7-3=4-3=1
        
        """
        res = 0
        turn = False
        if (dividend >=0 and divisor < 0):
            divisor = -divisor
            turn = True
        if (dividend < 0 and divisor >= 0):
            dividend = -dividend
            turn = True
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        while dividend >= divisor:
            res += 1
            dividend -= divisor
        if turn:
            res = -res
        return res
