class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(node, depth):
            if not node.left and not node.right:
                return node, depth

            left, l_depth = dfs(node.left, depth+1) if node.left else (node, depth)
            right, r_depth = dfs(node.right, depth+1) if node.right else (node, depth)

            if l_depth == r_depth:
                return node, l_depth
            
            return (left, l_depth) if l_depth > r_depth else (right, r_depth)

        lca, _ = dfs(root, 0)
        return lca
