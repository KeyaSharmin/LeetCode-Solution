class Solution:
  def maximumBeauty(self, nums: List[int], k: int) -> int:
    nums.sort()
    d = 2 * k
    l = 0
    for n in nums:
      if nums[l] + d < n:
        l += 1
    return len(nums) - l
