class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        return 8*sum(map(comb, Counter(starmap(mul, combinations(nums, 2))).values(), cycle([2])))
