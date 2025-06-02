class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = 1
        i = 1
        while i < n:
            while i < n and ratings[i] == ratings[i-1]:
                res += 1
                i += 1
            peak = 1
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1
                res += peak
                i += 1
            down = 1
            while i < n and ratings[i] < ratings[i-1]:
                res += down
                down += 1
                i += 1
            if down > peak:
                res += down - peak
        return res
