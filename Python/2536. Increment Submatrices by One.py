class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr = [[0] * (n) for _ in range(n)]

        for r1,c1,r2,c2 in queries:
            arr[r1][c1]+=1
            if c2<n-1: arr[r1][c2+1]-=1
            if r2<n-1: arr[r2+1][c1]-=1
            if c2<n-1 and r2<n-1: arr[r2+1][c2+1]+=1

        for i in range(n):
            k = 0
            for j in range(n):
                k+=arr[i][j]
                arr[i][j] = k

        for i in range(n):
            k = 0
            for j in range(n):
                k+=arr[j][i]
                arr[j][i] = k
        
        return arr
