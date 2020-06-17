class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        turn = False
        if dividend < 0:
            dividend = -dividend
            turn = not turn
        if divisor < 0:
            divisor = -divisor
            turn = not turn
        i = 0
        while dividend - divisor >= 0:
            dividend -= divisor
            diviosr = divisor << 1
            i += 1
        if turn:
            i = -i
        return i
