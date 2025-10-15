class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prevl = 1
        l = 1
        longest = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                longest = max(longest, min(l, prevl), l // 2)
                prevl = l
                l = 1
            else:
                l += 1
        
        longest = max(longest, min(l, prevl), l // 2)
        return longest
