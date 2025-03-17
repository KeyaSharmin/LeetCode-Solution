class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for num in count.values():
            if(num & 1) != 0:
                return False
        return True
