class Solution:
    def maxFreeTime(self, t: int, k: int, s: List[int], e: List[int]) -> int:
        q = [*map(sub,s+[t],[0]+e)]
        return max(accumulate(map(sub,q[k+1:],q),initial=sum(q[:k+1])))
