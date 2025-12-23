class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        starts = sorted(events)
        ends = sorted(events, key=lambda x: x[1])
        i = 0
        best_before = 0
        result = 0
        for start, end, value in starts:
            while ends[i][1] < start:
                best_before = max(best_before, ends[i][2])
                i += 1
            result = max(result, best_before + value)
        return result
