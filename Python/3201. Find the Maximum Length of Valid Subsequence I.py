class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_prev_p = 0
        odd_prev_q = 0
        even_prev_p = 0
        even_prev_q = 0
        for num in nums:
            if num % 2 == 1:
                odd_prev_p += 1
                odd_prev_q = 1 + even_prev_q
            else:
                even_prev_p += 1
                even_prev_q = 1 + odd_prev_q
        return max(odd_prev_p, odd_prev_q, even_prev_p, even_prev_q)
