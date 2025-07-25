class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums)<0 :
            return max(nums)
        else:
            result=0
            nums=set(nums)
            for i in nums:
                if i>=0:
                    result+=i
            return result
