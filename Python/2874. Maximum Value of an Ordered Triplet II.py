class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        highestSeen = 0
        highestDiff = 0
        ans = 0
        for num in nums:
            if (t:=(highestDiff*num)) > ans:
                ans = t
            if (t:=(highestSeen-num)) > highestDiff:
                highestDiff = t
            if num > highestSeen:
                highestSeen = num
        return ans
