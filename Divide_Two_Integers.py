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

   # v2
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
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
        print('dividend ' + str(dividend))
        print('divisor ' + str(divisor))
        if dividend < divisor:
            return 0
        if dividend == divisor:
            if turn:
                return -1
            else:
                return 1
        arr = []
        arr.append(divisor)
        ext = 0
        while dividend >= divisor:
            sub = dividend - arr[-1] - arr[-1] - divisor
            print('sub ' + str(sub))
            if sub < 0:
                for j in range(1, len(arr) + 1):
                    if j == len(arr) and arr[j-1] < dividend:
                        ext = j
                        print('j ' + str(j))
                        break
                    if arr[j - 1] > dividend - arr[-1]:
                        ext = j - 1
                        print('j ' + str(j - 1))
                        break
                break
                
            else:       
                
                dividend -= arr[-1]
                arr.append(arr[-1] + divisor)
                print('add')
                print(dividend)
                print(sub)
                print(arr)
                print('end add')
            print('dividend ' + str(dividend))
        count = 0
        for i in range(1, len(arr) + 1):
            count += i
        print(arr)
        print('count ' + str(count))
        print('ext ' + str(ext))
        count += ext
        if turn:
            count = -count
        return count

            
        
