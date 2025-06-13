class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0:
            return 0
        n = len(nums)
        nums.sort()
        all_dist = [nums[i+1]-nums[i] for i in range(n-1)]
        num_of_dist = len(all_dist)

        min_dist, max_dist = min(all_dist), max(all_dist)
        while min_dist<max_dist:
            mid = (min_dist+max_dist)//2
            k = 0
            i = 0
            while i<num_of_dist:
                if all_dist[i]<=mid:
                    k += 1
                    i += 2
                else:
                    i += 1
            if k<p:
                min_dist = mid+1
            else:
                max_dist = mid
        return max(max_dist,min_dist)
