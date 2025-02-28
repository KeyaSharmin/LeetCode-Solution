class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        memo = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if str1[i] == str2[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
                else:
                    if memo[i + 1][j] > memo[i][j + 1]:
                        memo[i][j] = memo[i + 1][j]
                    else:
                        memo[i][j] = memo[i][j + 1]
        res: str = ""
        i = 0
        j = 0
        while i < n and j < m:
            if str1[i] == str2[j]:
                res += str1[i]
                i += 1
                j += 1
            elif memo[i + 1][j] >= memo[i][j + 1]:
                res += str1[i]
                i += 1
            else:
                res += str2[j]
                j += 1
        if j < m:
            res += str2[j:]
        if i < n:
            res += str1[i:]

        return res
