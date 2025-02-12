class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = defaultdict(int)
        max_sum = -1
        for n in nums:
            digit_sum = 0
            curr_digit = n
            while curr_digit > 0:
                digit_sum += curr_digit % 10
                curr_digit = curr_digit // 10

            if digit_sum in sums:
                max_sum = max(max_sum, sums[digit_sum] + n)
            sums[digit_sum] = max(sums[digit_sum], n)

        return max_sum
