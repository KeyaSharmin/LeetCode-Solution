class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n == k:
            return 1
        if n < k:
            return 0
        MOD = 10**9 + 7
        cnts = []
        ans = 1
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                if cnt > 1:
                    if k > 0:
                        cnts.append(cnt - 1)
                    ans = ans * cnt % MOD
                k -= 1 
                cnt = 0
        num_char = len(cnts)
        if k <= 0:
            return ans  
        f = [0]*(k) 
        f[0] = 1
        for i in range(num_char):
            c = cnts[i]
            for j in range(1,k):
                f[j] = (f[j] + f[j-1]) % MOD
            for j in range(k-1, c, -1):
                f[j] -= f[j-c-1]

        return (ans - sum(f)) % MOD
