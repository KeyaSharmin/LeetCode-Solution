class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        res = 0
        low = -1
        for high, num in enumerate(nums):
            cur_sum += num
            while low < high and cur_sum * (high - low) >= k:
                low += 1
                cur_sum -= nums[low]
            res += high - low
        return res
