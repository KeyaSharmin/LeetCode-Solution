class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        day = idx = res = 0
        n = len(events)
        pq = []
        while idx < n or pq:
            if not pq:
                day = events[idx][0]
            while idx < n and events[idx][0] <= day:
                heapq.heappush(pq ,events[idx][1])
                idx += 1
            heapq.heappop(pq)
            res += 1
            day += 1
            while pq and pq[0] < day:
                heapq.heappop(pq)
        return res
