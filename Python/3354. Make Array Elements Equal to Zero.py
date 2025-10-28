class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        t = sum(nums)
        s = 0 
        ans = 0 
        for i in range(n):
            ts = t - s 
            if nums[i] == 0:
                if ts == s:
                    ans += 2 
                elif abs(ts-s) == 1:
                    ans += 1 
            s += nums[i]
        return ans
