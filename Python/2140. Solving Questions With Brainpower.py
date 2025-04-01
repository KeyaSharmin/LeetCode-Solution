class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        tp = [0]*n
        prev = questions[-1][0]
        for i in range(n-1, -1, -1):
            tp[i]= prev
            p, b = questions[i]
            j = i+b+1
            if j < n:
                p += tp[j]
            if p > prev:
                tp[i] = p
            prev = tp[i]
        return tp[0]
