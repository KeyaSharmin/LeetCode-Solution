class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_score = 0
        best_half_score = 0
        for value in values:
            best_half_score -= 1
            if best_half_score + value > best_score:
                best_score = best_half_score + value
            if value > best_half_score:
                best_half_score = value
        return best_score
