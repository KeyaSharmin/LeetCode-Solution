class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = 1 << 0

        for num in nums:
            dp |= dp << num

        return (dp & (1 << target)) != 0
