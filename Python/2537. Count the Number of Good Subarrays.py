class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        n, l, ans, dic, cnt = len(nums), 0, 0, {}, 0

        for a in nums:
            cnt += dic.get(a, 0)
            dic[a] = dic.get(a, 0)+1

            while cnt>=k:
                dic[nums[l]]-=1
                cnt -= dic[nums[l]]
                l+=1

            ans += l
        return ans
