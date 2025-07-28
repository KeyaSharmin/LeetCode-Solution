class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        prevBits = Counter([0])
        for num in nums:
            for prev, count in list(prevBits.items()):
                prevBits[prev | num] += count
        return prevBits[reduce(lambda a,b: a | b, nums)]
