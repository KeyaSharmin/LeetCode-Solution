class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        r=' '.join(words)
        s=[i for i in words if r.count(i)>1]
        return s
