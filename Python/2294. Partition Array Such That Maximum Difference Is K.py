class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        start = nums[0]
        groups = 1
        for num in nums:
            if num - start > k:
                groups += 1
                start = num
        return groups
