class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        a = [1]
        for i in nums:
            while (d:=gcd(a[-1],i))!=1:
                i = a.pop() * i//d
            a.append(i)
        return a[1:]
