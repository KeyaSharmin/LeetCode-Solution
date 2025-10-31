class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited = set()
        result = []
        for num in nums:
            if num in visited:
                result.append(num)
            else:
                visited.add(num)
        return result
