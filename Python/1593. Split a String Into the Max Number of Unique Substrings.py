class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        word=set()
        n, maxCnt=len(s), 0
        def f(i, cnt, s):
            nonlocal n, maxCnt
            if n-i<=maxCnt-cnt: return #prune
            if  i>=n:
                maxCnt=max(maxCnt, cnt)
                return
            t=""
            for j in range(i, n):
                t+=s[j]
                if t in word: continue
                word.add(t)
                f(j+1, cnt+1, s)
                word.remove(t)
        f(0, 0,s)
        return maxCnt
             