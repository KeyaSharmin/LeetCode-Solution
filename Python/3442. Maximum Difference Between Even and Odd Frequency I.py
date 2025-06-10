class Solution:
    def maxDifference(self, s: str) -> int:
        s = sorted(s)
        mx_odd = 0
        min_even = float('inf')
        cur = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == cur:
                cnt += 1
            else:
                if cnt % 2 == 1:
                    mx_odd = max(mx_odd, cnt)
                else:
                    min_even = min(min_even, cnt)
                cur = s[i]
                cnt = 1
        if cnt % 2 == 1:
            mx_odd = max(mx_odd, cnt)
        else:
            min_even = min(min_even, cnt)

        return mx_odd - min_even
