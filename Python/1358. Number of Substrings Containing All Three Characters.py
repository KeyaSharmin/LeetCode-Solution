class Solution:
    def numberOfSubstrings(self, s):
        n = len(s)
        arr = [-1, -1, -1]
        cnt = 0
        for i in range(n):
            ch = s[i]
            arr[ord(ch) - ord('a')] = i
            cnt += 1 + min(arr)
        return cnt
