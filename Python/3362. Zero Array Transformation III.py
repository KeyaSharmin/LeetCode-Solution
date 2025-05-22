class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        n, edges = len(nums), defaultdict(list)
        for start, end in queries:
            edges[start].append(end)

        lines, heap, current = [0] * (n + 1), [], 0
        for num_index, num in enumerate(nums):
            if num_index in edges:
                for end in edges[num_index]: heappush(heap, -end)

            current += lines[num_index]
            while current < num:
                if not heap or -heap[0] < num_index: return -1
                end = -heappop(heap)
                current += 1
                lines[end + 1] -= 1

        return len(heap)
