from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        self.ans = []
        def generate_good(i, m, curNum, counter):
            if i == m:
                good = True
                for key in counter.keys():
                    if counter[key] == 0:
                        continue
                    elif counter[key] != key:
                        good = False
                        break
                if good:
                    self.ans.append(curNum)
                return
            for newDig in range(1, m+1):
                if counter[newDig] == newDig or counter[newDig] + m - i < newDig:
                    continue
                counter[newDig] += 1
                generate_good(i+1, m, curNum*10 + newDig, counter)
                counter[newDig] -= 1 
            return
        
        generate_good(0, len(str(n)), 0, defaultdict(int))
        if max(self.ans) <= n:
            self.ans = []
            generate_good(0, len(str(n)) + 1, 0, defaultdict(int))
        for num in self.ans:
            if num > n:
                return num
        
