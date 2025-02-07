class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colours = {}
        res = []
        for b, c in queries:
            if b in balls:
                if colours[balls[b]] == 1:
                    del colours[balls[b]]
                else:
                    colours[balls[b]] -= 1
            colours[c] = colours.get(c, 0) + 1
            balls[b] = c
            res.append(len(colours))
        
        return res
