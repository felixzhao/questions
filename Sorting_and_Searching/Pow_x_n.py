class Solution:
    def myPowBruteForce(self, x: float, n: int) -> float:
        """
        Brute Force

        time  O(N)
        space O(1)

        key point
            - if n < 0, must set to -n
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        res = x
        for i in range(n - 1):
            res *= x
            # print(f'{i} {res}')
        return res