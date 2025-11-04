class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result=[]
        d={}
        for i in range(k):
            d[nums[i]]=d.get(nums[i],0)+1
        sorted_items = sorted(d.items(), key=lambda item: (item[1], item[0]), reverse=True)
        result.append(sum(num * count for num, count in sorted_items[:x]))
        for i in range(k,len(nums)):
            left=nums[i-k]
            right=nums[i]
            if left in d:
                d[left]-=1
                if d[left]==0:
                    del d[left]
            d[right]=d.get(right,0)+1
            sorted_items = sorted(d.items(), key=lambda item: (item[1], item[0]), reverse=True)
            result.append(sum(num * count for num, count in sorted_items[:x]))
        return result
