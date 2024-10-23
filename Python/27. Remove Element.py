class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)

        k = len(nums)
        return k
        