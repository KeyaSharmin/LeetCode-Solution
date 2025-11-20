class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        output = 0
        a, b = float("-inf"), float("-inf")
        for i, j in intervals:
            if i > b:
                output += 2
                a, b = j - 1, j
            elif i > a:
                output += 1
                a, b = b, j
        return output
