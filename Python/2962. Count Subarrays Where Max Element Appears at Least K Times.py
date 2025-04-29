class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        maxN = max(nums)
        left = ans = 0
        for right in nums:
            if right == maxN:
                cnt += 1
            while cnt >= k:
                if nums[left] == maxN:
                    cnt -= 1
                left += 1
            ans += left
        return ans
