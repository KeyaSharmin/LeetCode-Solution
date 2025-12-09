class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        pair = defaultdict(int)
        ans = 0
        MOD = 10**9 + 7
        for n in nums:
            if n in cnt:
                ans += pair[n] % MOD
            if n * 2 in cnt:
                pair[n * 2] += cnt[n * 2] % MOD
            cnt[n] += 1
        return ans % MOD
