class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        ans = 0
        d = defaultdict(int)
        d[0] = 1
        w = 0
        for i in nums:
            if i % modulo == k:
                w += 1
            r = w % modulo
            ans += d[(r - k) % modulo]
            d[r] += 1
        return ans
