class Solution:
    def maximumLength(self, s: str) -> int:
        cnt_dict = defaultdict(list)
        cnt = 0
        current_c = None
        s = s + "1"
        for c in s:
            if not current_c:
                current_c = c
            if current_c == c:
                cnt += 1
            else:
                cnt_dict[current_c].append(cnt)
                current_c = c
                cnt = 1
        ans = -1
        for k, v in cnt_dict.items():
            v = sorted(v, reverse=True)
            if v[0] > 2:
                ans = max(v[0]-2, ans)
            if len(v) >= 2 and v[0] > 1:
                    ans = max(min(v[0]-1, v[1]), ans)
            if len(v) >= 3:
                ans = max(ans, v[2])

        return ans
