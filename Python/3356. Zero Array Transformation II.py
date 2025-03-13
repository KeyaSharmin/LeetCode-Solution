class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        k = 0
        prefix = [0]*(len(nums)+1)
        cur_sum = 0
        cur_interval = 0
        for i in range(n):
            cur_sum += prefix[i]
            if cur_sum >= nums[i]:
                continue
            else:
                while k < len(queries) and cur_sum < nums[i]:
                    start, end, val = queries[k]
                    if start <= i:
                        cur_sum += val
                    else:
                        prefix[start] += val
                    if end + 1 <= i:
                        cur_sum -= val
                    else:
                        prefix[end+1] -= val
                    k+=1
                if k == len(queries) and cur_sum < nums[i]:
                    return -1
        return k
                    
