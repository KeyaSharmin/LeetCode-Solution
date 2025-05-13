dp = [1] * (100_000 + 26)
for i in range(26, len(dp)):
    dp[i] = (dp[i-26] + dp[i-25]) % 1_000_000_007

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ans = 0
        cnt = Counter(s)
        for k, v in cnt.items():
            ans = (ans + v * dp[(ord(k) - 97) + t]) % 1_000_000_007
        return ans
