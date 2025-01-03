class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        res = 0
        n = abs(x)
        while n != 0:
            res = res * 10 + n % 10
            if res > 2**31-1:
                return 0
            n //= 10
        
        return res * sign  