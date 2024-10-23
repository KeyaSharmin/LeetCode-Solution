from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        score_dict = {}
        
        # Build a trie and count prefix scores
        for word in words:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                    cur[char]['#'] = 0
                cur[char]['#'] += 1
                cur = cur[char]
        
        # Calculate scores for each word
        def calculateScore(word):
            score = 0
            cur = trie
            for char in word:
                score += cur[char]['#']
                cur = cur[char]
            return score

        return [calculateScore(word) for word in words]  