class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        temp_count = 1
        n = len(nums)
        max_v = 1
        for i in range (1, n):
            if nums[i] > nums[i-1]:
                temp_count += 1
                max_v = max(temp_count, max_v)
            else:
                temp_count = 1
        temp_count = 1
        for i in range (1,n):
            if nums[i] < nums[i-1]:
                temp_count += 1                
                max_v = max(temp_count, max_v)
            else:
                temp_count = 1
        return max_v
