class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n=len(complexity)
        if n==0:
            return 0
        t=complexity[0]
        for i in range(1,n):
            if complexity[i]<=t:
                return 0
        result=1
        for i in range(1,n):
            result=(result*i)%(10**9 + 7)
        return result
