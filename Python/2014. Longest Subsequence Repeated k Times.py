class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        s = [ord(c) - ord('a') for c in s]
        cnt = Counter(s)
        possible = {c for c, v in cnt.items() if v >= k}
        possible_sort = sorted(possible)
        s = tuple(c for c in s if c in possible)
        n = len(s)
        l = n // k
        poses = [-1] * 26
        nextchar = []
        stat = [0] * 26
        for i in reversed(range(n)):
            c = s[i]
            stat[c] += 1
            nextchar.append(poses[:])
            poses[c] = i
        nextchar = nextchar[::-1]
        nextchar.append(poses[:])
        def check(word, idx=-1, tot=k):
            nonlocal n, nextchar
            for _ in range(tot):
                for c in word:
                    idx = nextchar[idx][c]
                    if idx < 0:
                        return False
            return True

        result = []
        
        def prep(idx, word, wordstat):
            nonlocal result
            for c in reversed(possible_sort):
                word.append(c)
                wordstat[c] += 1
                if stat[c] >= wordstat[c] * k and check(word, -1, k):
                    if len(word) > len(result) or len(word) == len(result) and word > result:
                        result = word[:]
                    prep(idx, word, wordstat)
                wordstat[c] -= 1
                word.pop()

        prep(0, [], [0] * 26)

        return ''.join(chr(c + ord('a')) for c in result)
    
