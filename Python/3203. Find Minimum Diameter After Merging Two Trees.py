class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n, m = len(edges1) + 1, len(edges2) + 1
        d1 = self.get_diameter(n, edges1)
        r1 = (d1 + 1) // 2
        d2 = self.get_diameter(m, edges2)
        r2 = (d2 + 1) // 2
        return max(d1, d2, 1 + r1 + r2)

    def get_diameter(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return 0

        graph = [[] for _ in range(n)]
        degree = [0] * n
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)
            degree[v] += 1
            degree[w] += 1

        leaves = deque(v for v in range(n) if degree[v] == 1)
        tree_size = n
        radius = 0
        while tree_size > 2:
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                tree_size -= 1
                degree[leaf] -= 1
                for nxt in graph[leaf]:
                    degree[nxt] -= 1
                    if degree[nxt] == 1:
                        leaves.append(nxt)
            radius += 1

        return 2 * radius + (tree_size == 2)
