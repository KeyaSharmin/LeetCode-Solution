class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        curr = {0}
        for x in arr:
            now = {x}
            for y in curr:
                now.add( y|x )
            curr = now
            ans |= curr
        return len(ans)
