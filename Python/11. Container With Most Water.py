class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        result, current = 0, 0
        p = max(height)
        while low < high:
            current = (high - low) * min(height[high], height[low])
            if current > result:
                result = current
            elif height[high] > height[low]:
                low += 1
            else:
                high -= 1
            if (high - low) * p < result:
                break
        return result