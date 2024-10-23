from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        n1set, n2set = set(), set()

        for n1 in arr1:
            while n1 and n1 not in n1set:
                n1set.add(n1)
                n1 = n1 // 10
        
        for n2 in arr2:
            while n2 and n2 not in n2set:
                n2set.add(n2)
                n2 = n2 // 10
        res = 0
        for n in n1set:
            if n in n2set:
                res = max(res, len(str(n)))
        return res