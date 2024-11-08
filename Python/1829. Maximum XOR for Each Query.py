class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = [(1 << maximumBit) - 1]
        for n in nums:
            ans.append(ans[-1] ^ n)

        return ans[len(ans)-1:0:-1]
