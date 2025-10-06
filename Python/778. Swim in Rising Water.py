class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = []
        heapq.heappush(minHeap, [grid[0][0],0,0])
        visited = set()
        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        while minHeap:
	        max_height, i,j = heapq.heappop(minHeap)
	        
	        if i == n-1 and j == n-1:
		        return max_height
	        for dr, dc in directions:
		        r, c = dr+i, dc+j
		        if 0<=r<n and 0<=c<n and (r,c) not in visited:
		            visited.add((r,c))
		            heapq.heappush(minHeap, [max(max_height, grid[r][c]), r,c])
        return -1
