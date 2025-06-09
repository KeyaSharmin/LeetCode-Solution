class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(prefix, limit):
            lb, rb = prefix, prefix
            ans = 0
            while lb <= limit:
                ans += min(limit, rb) - lb + 1
                lb *= 10
                rb = rb * 10 + 9
            return ans

        prefix = 1
        while k > 1:
            cnt = count(prefix, n)
            if cnt < k:
                k -= cnt
                prefix += 1
            else:
                prefix *= 10
                k -= 1
        return prefix
