class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(x):
            if x==0:
                return True
            return sum([candy//x for candy in candies])>=k
        
        left = 0
        right = sum(candies)//k

        while left<=right:
            mid = (left+right)//2
            if check(mid):
                left = mid+1
            else:
                right = mid-1
        return right
