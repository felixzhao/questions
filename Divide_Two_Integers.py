"""
when number double value during iterator
We need to think about the bit move
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        turn = False
        if dividend < 0:
            dividend = -dividend
            turn = not turn
        if divisor < 0:
            divisor = -divisor
            turn = not turn
        i = 0
        while dividend >= divisor:
            """
            t = 9
            j = 4
            div = 1
            i = 2
            
            """
            temp, j = divisor, 1
            while dividend >= temp:
                dividend -= temp
                temp <<= 1
                i += j # add j step
                j <<= 1
        if turn:
            i = -i
        return i
    
    """
    Good version
    """
    def divide(self, dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)
