class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        result = 0
        for i, (_, top) in enumerate(points):
            bot = -inf
            for (_, y) in points[i + 1:]:
                if bot < y <= top:
                    result += 1
                    bot = y
                    if top == bot:
                        break
        return result
