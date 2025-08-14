class Solution:
    def largestGoodInteger(self, num: str) -> str:
        arr = [""]
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                arr.append(num[i] * 3)
        sorted_arr = sorted(arr)
        max_elem = sorted_arr[-1]
        return max_elem
        
