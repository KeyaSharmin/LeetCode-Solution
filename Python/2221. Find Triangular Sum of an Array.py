class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i, v in enumerate(nums):
            res += v * comb(n - 1, i)
        
        return res % 10
