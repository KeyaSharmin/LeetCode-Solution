class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def dfs(i, idx, viz):
            if viz[i]: return 0
            viz[i]=True
            j=idx[i]
            return 1+dfs(j, idx, viz)

        q=deque()
        q.append(root)
        swaps=0
        while q:
            qz=len(q)
            arr=[0]*qz
            for i in range(qz):
                node=q.popleft()
                arr[i]=node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            idx=sorted(range(qz), key = lambda k : arr[k])

            viz=[False]*qz
            for i in range(qz):
                if not viz[i]:
                    swaps+=dfs(i, idx, viz)-1
        return swaps
