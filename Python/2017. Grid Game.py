class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        one, two = sum(grid[0]), 0
        for x, y in zip(*grid):
            one -= x
            two += y
            if two > one:
                return max(one, two - y)
