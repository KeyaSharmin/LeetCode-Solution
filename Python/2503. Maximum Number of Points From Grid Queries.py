class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [0] * len(queries)
        heap = [(grid[0][0], 0, 0)]
        directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        grid[0][0] = 0
        cnt = 0
        for qi, q in sorted(enumerate(queries), key=lambda x: x[1]):
            while heap and heap[0][0] < q:
                _, i, j = heappop(heap)
                cnt += 1
                for di, dj in directions:
                    inew, jnew = i+di, j+dj
                    if inew>=0 and inew<m and jnew>=0 and jnew<n and grid[inew][jnew]:
                        heappush(heap, (grid[inew][jnew], inew, jnew))
                        grid[inew][jnew] = 0
            res[qi] = cnt
        return res
