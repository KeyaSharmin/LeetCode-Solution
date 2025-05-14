import numpy as np
MOD = 10**9 + 7
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        base,cur = np.zeros((26,26), dtype=object), np.eye(26, dtype=object)
        for i,v in enumerate(nums):
            for j in range(i+1, i+v+1):
                base[i][j%26]=1
        def mul(a,b):
            c = np.dot(a,b)
            for i,j in product(range(26),repeat=2):
                c[i][j]%=MOD
            return c
        while t:
            if t&1>0: cur=mul(cur,base)
            base=mul(base,base)
            t>>=1
        data=[sum(r)%MOD for r in cur]
        return sum(data[ord(ch)-97] for ch in s)%MOD
        
