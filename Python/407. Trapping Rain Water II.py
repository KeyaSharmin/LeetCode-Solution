class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap=[]

        m=len(heightMap)
        n=len(heightMap[0])

        visited=[[False for _ in range(n)] for _ in range(m)]
        #store boundries
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    heapq.heappush(heap,(heightMap[i][j],i,j))
                    visited[i][j]=True

        dir=[[0,1],[0,-1],[1,0],[-1,0]]

        #bfs
        trapped_water=0
        while heap:
            height, i ,j = heapq.heappop(heap)
            for x,y in dir:
                newX=x+i
                newY=y+j
                if 0<newX<m and 0<newY<n and not visited[newX][newY]:
                    visited[newX][newY]=True
                    cell_height=heightMap[newX][newY]
                    if cell_height< height:
                        trapped_water+=height-cell_height
                        heapq.heappush(heap, (height,newX,newY))
                    else:
                        heapq.heappush(heap, (cell_height,newX,newY))
                
        return trapped_water
