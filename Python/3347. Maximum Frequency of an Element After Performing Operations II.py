class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        left = 0
        right = 0
        i = 0 
        while i < n:
            x = nums[i]
            j = i 
            cnt_x = 0
            while j < n and nums[j] == x:
                cnt_x += 1
                j += 1
            while left < n and nums[left] < x - k:
                left += 1
            while right < n and nums[right] <= x + k:   
                right += 1
            res = max(res, min(right - left, cnt_x + numOperations))
            i = j
        if res >= numOperations:
            return res 
        res_no_x = 0
        left = 0
        for right, x in enumerate(nums):
            while nums[left] < x - k * 2:
                left += 1
            res_no_x = max(res_no_x, right - left + 1)
        res_no_x = min(res_no_x, numOperations)
        return max(res, res_no_x)  
