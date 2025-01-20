class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        v2p = {}
        m,n=len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                v2p[mat[r][c]] = (r,c)
        
        rows = [0]*m
        cols = [0]*n

        for i in range(m*n):
            r, c = v2p[arr[i]]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i
        return -1
