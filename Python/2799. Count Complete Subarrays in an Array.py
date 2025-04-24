class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        complete = 0
        count = collections.Counter()
        i = 0
        for j in range(len(nums)):
            count[nums[j]] += 1
            while len(count) == distinct:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    del count[nums[i]]
                i += 1
            complete += i
        return complete
