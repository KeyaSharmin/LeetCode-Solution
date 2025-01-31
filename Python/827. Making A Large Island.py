class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def explore_land(start): 
            queue = [start] 
            water = set() 
            area = 1
            while queue:
                i, j = queue.pop()
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj 
                    if 0 <= ni < m and 0 <= nj < n: 
                        if grid[ni][nj] == 1: 
                            grid[ni][nj] = -1 
                            queue.append((ni,nj)) 
                            area += 1 
                        elif grid[ni][nj] == 0: 
                            water.add((ni,nj))
            for cell in water: 
                water_area[cell] += area
        m, n= len(grid), len(grid[0]) 
        water_area = defaultdict(int) 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    grid[i][j] = -1 
                    explore_land((i,j))
        if water_area:
            return 1 + max(water_area.values()) 
        return 1 if grid[0][0] == 0 else m*n 
