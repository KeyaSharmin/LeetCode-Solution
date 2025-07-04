class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        bits = k.bit_length()
        res = 0
        for i in range(bits):
            if (k >> i) & 1:
                res += operations[i]
        return chr(ord('a') + (res % 26))
