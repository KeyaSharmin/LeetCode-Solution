class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:return 0
        cost_cut = [weights[i-1]+weights[i] for i in range(1, len(weights))]
        cost_cut.sort()
        
        return sum(cost_cut[-k+1:]) - sum(cost_cut[:k-1])
