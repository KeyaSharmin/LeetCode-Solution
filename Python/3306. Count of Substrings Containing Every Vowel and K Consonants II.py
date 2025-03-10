class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        res = 0
        vowels = set('aeiou')
        n = len(word)
        freq = defaultdict(int)
        lo, hi, cnt = 0, 0, 0
        for c in word:
            if c in vowels:
                freq[c] += 1
            else:
                cnt += 1
            while cnt > k:
                if word[hi] in vowels:
                    freq[word[hi]] -= 1
                    if freq[word[hi]] == 0:
                        del freq[word[hi]]
                else:
                    cnt -= 1
                hi += 1
                lo = hi
            while cnt == k and hi < n:
                if word[hi] in vowels and freq[word[hi]] > 1:
                    freq[word[hi]] -= 1
                    if freq[word[hi]] == 0:
                        del freq[word[hi]]
                    hi += 1
                else:
                    break
            if cnt == k and len(freq) == 5:
                res += hi - lo + 1
        return res
