import numpy as np
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def p(n):
            sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
            sieve[0] = False
            for i in range(int(n**0.5)//3+1):
                if sieve[i]:
                    k=3*i+1|1
                    sieve[      ((k*k)//3)      ::2*k] = False
                    sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
            return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]
        a=p(right+1)
        idx=bisect.bisect_left(a,left)
        m=right
        out=[-1,-1]
        for a,b in pairwise(a[idx:]):
            if b-a<m:
                m=b-a
                out=[a,b]
        return list(map(int,out))

        print(a[idx:])
