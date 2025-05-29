class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def find_even(edges: list, n: int) -> list:
            graph = [[] for _ in range(n)] 
            queue = deque([(0, -1, True)])
            evens = [False] * n
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            while queue:
                node, parent, is_even = queue.popleft()
                evens[node] = is_even
                for child in graph[node]:
                    if child == parent: continue
                    queue.append((child, node, not is_even))

            return evens

        n1, n2 = len(edges1) + 1, len(edges2) + 1
        evens1, evens2 = find_even(edges1, n1), find_even(edges2, n2)
        sm1, sm2 = sum(evens1), sum(evens2)
        mx = max(sm2, n2 - sm2)
        ans = [mx + (sm1 if even else n1 - sm1) for even in evens1]

        return ans
