class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        - init res size with sum of two nums length (I have a bug here, not multi)
        - reverse two nums (string not list in python, need to use [::-1] to reverse)
        - same as we manual multi
          - from low to high, multi two number, put n1/n2 to pos, n1%n2 to the one higer pos
          - following n2 move, pos should move to 
          - after n1 multi with all n2 in num2, move pos to high
        - skip all start 0 in the res
        - transfer the result to string (here only take value from p, which is start point with skip 0)
        
        """
        res = [0] * (len(num1) + len(num2))
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        p = len(res) - 1

        for n1 in num1:
            sp = p
            for n2 in num2:
                res[sp] += int(n1) * int(n2)
               
                res[sp - 1] += int(res[sp] / 10)
               
                res[sp] = int(res[sp] % 10)
                
                sp -= 1
            p -= 1
        p = 0
        while (p < len(res) - 1) and (res[p] == 0):
            p += 1
        return ''.join(map(str, res[p:]))
            
