fmax = lambda x,y: x if x > y else y
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[1])
        n = len(events)
        dp = [[0]*(k+1) for _ in range(n+1)]
        ends = [e[1] for e in events]

        for i in range(n):
            s,e,v = events[i]
            end_before_me = bisect_right(ends,s-1)
            for j in range(1,k+1):
                dp[i+1][j] = fmax(dp[i][j],v + dp[end_before_me][j-1])

        return dp[-1][-1]
