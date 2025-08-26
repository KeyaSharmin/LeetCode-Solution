class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = max(a**2+b**2 for a,b in dimensions)
        return max(a*b for a, b in dimensions if a**2+b**2 == max_diag)
        max_diag = 0
        res = 0
        for a, b in dimensions:
            if a**2 + b**2 >= max_diag:
                max_diag = a**2 + b**2
                res = a*b
        return res
