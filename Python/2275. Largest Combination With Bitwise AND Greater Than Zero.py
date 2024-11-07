MAX_N_BITS = 24

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_set = 1 # Any one element is > 0
        mask = 1
        for shift in range(MAX_N_BITS):
            count = 0
            for num in candidates:
                if num & mask:
                    count += 1
            if max_set < count:
                max_set = count
            mask <<= 1
        return max_set
