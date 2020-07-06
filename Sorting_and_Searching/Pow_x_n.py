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

        def doPowFastPow(self, x: float, n: int) -> float:
            """
            Fast Pow

            time  O(logN)
            space O(logN)

            logic
                - x^8 = (x^4)^2
                - x^9 = (x^4)^2 * x

            key points
                - python int div must use  n//2, otherwise will return float
                - mode must trans to int (e.g int(n%2))

            """
            if n == 0:
                return 1.0
            t = self.doPow(x, n // 2)
            if int(n % 2) == 0:
                return t * t
            else:
                return t * t * x

        def myPow(self, x: float, n: int) -> float:
            if n < 0:
                x = 1 / x
                n = -n
            return self.doPow(x, n)
