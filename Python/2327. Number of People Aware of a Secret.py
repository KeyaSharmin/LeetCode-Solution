class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*n
        dp[0] = 1
        s = 0
        for i in range(delay,n):
            s += dp[i-delay]
            dp[i] = s
            if i-forget+1 >= 0:
                s -= dp[i-forget+1]
        return(sum(dp[-forget:]))%(10**9+7)
