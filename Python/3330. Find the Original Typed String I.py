class Solution:
    def possibleStringCount(self, word: str) -> int:
        p, cnt, ans = "", 0, 1
        for w in word:
            if w == p: cnt += 1
            else: ans += cnt; p, cnt = w, 0
        return ans + cnt
