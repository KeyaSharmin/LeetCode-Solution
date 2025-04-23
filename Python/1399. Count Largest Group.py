class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = [0] * 40
        rank = [0] * (n + 1)
        for i in range(1, n + 1):
            group = i % 10 + rank[i // 10]
            rank[i] = group
            cnt[group] += 1
        return cnt.count(max(cnt))
