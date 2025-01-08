class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                str1, str2 = words[j], words[i]
                if str1.startswith(str2) and str1.endswith(str2):
                    count += 1
        return count
