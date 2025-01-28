class Solution:
    def solve(self, i, j, grid, vis):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or vis[i][j] or grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        vis[i][j] = True
        temp += self.solve(i + 1, j, grid, vis)
        temp += self.solve(i - 1, j, grid, vis)
        temp += self.solve(i, j + 1, grid, vis)
        temp += self.solve(i, j - 1, grid, vis)
        return temp

    def findMaxFish(self, grid):
        self.m, self.n = len(grid), len(grid[0])
        ans = 0
        vis = [[False] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] != 0 and not vis[i][j]:
                    ans = max(ans, self.solve(i, j, grid, vis))
        return ans
