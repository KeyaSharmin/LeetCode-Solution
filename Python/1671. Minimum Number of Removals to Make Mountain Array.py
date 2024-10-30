from bisect import bisect_left


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        def getLis(arr):
            res = [0] * n
            stack = []
            for i in range(n):
                if stack and stack[-1] >= arr[i]:
                    j = bisect_left(stack, arr[i])
                    stack[j] = arr[i]
                    res[i] = j+1
                else:
                    stack.append(arr[i])
                    res[i] = len(stack)
            return res
        
        left, right = getLis(nums), getLis(nums[::-1])[::-1]
        #print(left, right)
        ans = float('inf')
        for i in range(n):
            if left[i] > 1 and right[i] > 1:
                ans = min(ans, n - (left[i] + right[i]-1))

        return ans