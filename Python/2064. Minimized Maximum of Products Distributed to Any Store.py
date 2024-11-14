class Solution:
    def isPossible(self, x: int, quantities: list[int], n: int) -> bool:
        sum = 0
        for u in quantities:
            sum += -(-u // x)  # Equivalent to ceil(u / x)
        return sum > n

    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        left, right = 1, 100000
        while left < right:
            mid = (left + right) // 2
            if self.isPossible(mid, quantities, n):
                left = mid + 1
            else:
                right = mid
        return left
