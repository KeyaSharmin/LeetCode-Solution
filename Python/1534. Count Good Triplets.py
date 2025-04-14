class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        mx = max(arr)
        s = [0] * (mx + 2)

        for j, y in enumerate(arr):
            for z in arr[j + 1:]:
                if abs(y - z) > b:
                    continue
                
                l = max(y - a, z - c, 0)
                r = min(y + a, z + c, mx)
                ans += max(s[r + 1] - s[l], 0)

            for v in range(y + 1, mx + 2):
                s[v] += 1
        return ans
        
    
