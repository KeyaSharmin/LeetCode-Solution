class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        d=list(range(len(nums)))
        ans=[]
        for i in range(1,len(nums)):
            if nums[i]%2 != nums[i-1]%2:
                d[i]=d[i-1]
        for frm, to in queries:
            if d[to] <= frm:
                ans.append(True)
            else:
                ans.append(False)
        return ans
