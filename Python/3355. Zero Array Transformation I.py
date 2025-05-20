class Solution:
    def isZeroArray(self, a: List[int], q: List[List[int]]) -> bool:
        b = [0]*(len(a)+1)
        for l,r in q:
            b[l] += 1
            b[r+1] -= 1
        
        return all(map(le,a,accumulate(b)))
