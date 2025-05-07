class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        row = len(moveTime)
        col = len(moveTime[0])
        direct = [0, 1, 0, -1, 0]
        hq = [(0, 0, 0)]
        visited = set()
        while hq:
            time, x, y = heappop(hq)
            if x == row - 1 and y == col - 1:
                return time
            for i in range(4):
                nx, ny = x + direct[i], y + direct[i + 1]
                if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    t = time + 1 if time >= moveTime[nx][ny] else moveTime[nx][ny] + 1
                    heappush(hq, (t, nx, ny))
