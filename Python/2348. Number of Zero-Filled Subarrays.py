class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
         count = 0
         zero_count = 0
         for num in nums:
             if num == 0:
                 zero_count += 1
                 count += zero_count
             else:
                  zero_count = 0
         return count
