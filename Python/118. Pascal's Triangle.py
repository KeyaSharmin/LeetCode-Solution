class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            result = [[1],[1,1]]
            return result
        result = [[1],[1,1]]
        for i in range(2, numRows):
            curr = []
            for j in range(i+1):
                print(j)
                if (j == 0) or (j == i):
                    curr.append(1)
                else:
                    val = result[i-1][j-1] + result[i-1][j]
                    curr.append(val)
            result.append(curr)
        return result
