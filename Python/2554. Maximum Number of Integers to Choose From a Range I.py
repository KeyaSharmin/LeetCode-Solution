class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count,total = 0,0
        for x in range(1,n+1):
            if x not in banned:
                if total + x > maxSum:
                    return count
                total += x
                count += 1
        return count
