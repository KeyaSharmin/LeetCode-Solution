class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n=1
        res=0
        prev=float('inf')
        for price in prices:
            if prev-price==1:
                n+=1
            else:
                res+=(n*(n+1))//2
                n=1
            prev=price
        res+=(n*(n+1))//2
        return res-1
        
