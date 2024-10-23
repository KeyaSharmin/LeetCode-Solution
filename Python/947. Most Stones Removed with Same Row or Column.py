class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """

        parent = [i for i in range(len(stones))] 
        size = [1 for i in range(len(stones))]  
        self.num_groups = len(stones)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            root1, root2 = find(x), find(y)     
            if root1 == root2: return 

            if size[root1] < size[root2]:
                size[root2] += size[root1]
                parent[root1]= root2
                size[root1] = 0
            else:
                size[root1] += size[root2]
                parent[root2]= root1
                size[root2] = 0

            self.num_groups -= 1

        row_dict = dict()
        col_dict = dict()

        for i, stone in enumerate(stones):
            r, c = stone
            if r in row_dict:
                union(i, row_dict[r])
            else:
                row_dict[r] = i

            if c in col_dict:
                union(i, col_dict[c])
            else:
                col_dict[c] = i

        return len(stones) - self.num_groups