class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        pfs = list(accumulate(differences, initial = 0))

        return max(0, upper - lower - max(pfs) + min(pfs) + 1)
