class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(baskets)
        s = 1
        while s < n:
            s *= 2
        t = [0] * (2 * s)
        
        for i in range(n):
            t[s + i] = baskets[i]
        for i in range(s - 1, 0, -1):
            t[i] = max(t[2 * i], t[2 * i + 1])
        
        c = 0
        for x in fruits:
            if t[1] < x:
                c += 1
            else:
                i = 1
                while i < s:
                    if t[2*i] >= x:
                        i = 2*i
                    else:
                        i = 2*i+1
                j = i - s
                t[i] = -1
                i //= 2
                while i:
                    t[i] = max(t[2*i], t[2*i+1])
                    i //= 2
        return c
