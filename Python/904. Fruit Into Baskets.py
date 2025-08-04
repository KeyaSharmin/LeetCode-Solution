class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0
        f1, f2 = -1, -1
        count1, count2 = 0, 0
        prev = 0
        for f in fruits:
            if f == f1:
                count1 += 1
                prev += 1
            elif f == f2:
                f1, f2 = f2, f1
                count1, count2 = count2 + 1, count1
                prev = 1
            else:
                result = max(result, count1 + count2)
                f1, f2 = f, f1
                count1, count2 = 1, prev
                prev = 1
        return max(result, count1 + count2)
