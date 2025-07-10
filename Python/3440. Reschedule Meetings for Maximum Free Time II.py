class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        startTime = startTime + [eventTime]
        endTime = [0] + endTime
        largest_free = nlargest(3, ((e-s, s) for e, s in zip(startTime, endTime)))
        ans = 0
        for (e1, s1), (e2, s2) in pairwise(zip(startTime, endTime)):
            event = s2-e1
            free = e1-s1 + e2-s2
            for max_free, s in largest_free:
                if s1 != s and s2 != s and event <= max_free:
                    ans = max(free + event, ans)
                    break
            else:
                ans = max(free, ans)
        return ans
