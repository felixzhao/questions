class Solution:
    def find(self, n: int, m: int) -> List[str]:
        """
        Recursive

        understand question is harder than resolve it

        - explain the question by case
            - 0 [""]
            - 1 ["0","1","8"]
            - 2 ["11","69","88","96"]
            - 3 ["101","111","181","609","619","689","808","818","888","906","916","986"]
-4 ["1001","1111","1691","1881","1961","6009","6119","6699","6889","6969","8008","8118","8698","8888","8968","9006","9116","9696","9886","9966"]

        - logic
            - recusive n-2
            - if n = 0 return empty string
            - n = 1 return case 1
            - if not last round add 0s0
            - always add 1s1,8s8,6s9,9s6

        - key points
            - because n-2
            - so odd always decrease to 1, return ['0','1','8']
            - and even always decrease to 0, ['']

        time  ???
        space ???

        """
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        res = self.find(n - 2, m)
        nums = []
        if n != m:
            nums = ['0' + s + '0' for s in res]
        return nums + [a + s + b for a, b in ['11', '88', '69', '96'] for s in res]

    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.find(n, n)

