class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        residuals =[0] * value
        for n in nums:
            residuals[n % value] += 1
        minloop = min(residuals)
        ind = residuals.index(minloop)
        return minloop * value + ind
