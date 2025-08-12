class Solution:
    def numberOfWays(self, n, x):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for a in range(1, n + 1):
            ax = a**x
            if ax <= n:
                for i in range(n, ax - 1, -1):
                    dp[i] = (dp[i] + dp[i - ax])
            else:
                break

        return dp[n]% MOD
