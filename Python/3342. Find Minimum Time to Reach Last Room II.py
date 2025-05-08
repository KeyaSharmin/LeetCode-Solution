class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        visited = [[0]*cols for _ in range(rows)]
        heap = [(0,0,0,1)]
        resp = 0
        while heap:
            time, r, c, carry = heapq.heappop(heap)
            resp = time
            if r == rows-1 and c == cols-1:
                break
            for i,j in [(r-1,c), (r+1,c), (r, c-1), (r,c+1)]:
                if 0 <= i < rows and 0 <= j < cols and not visited[i][j]:
                    temp = max(time, moveTime[i][j])+carry
                    heapq.heappush(heap, (temp,i,j,3-carry))
                    visited[i][j] = 1
        return resp
