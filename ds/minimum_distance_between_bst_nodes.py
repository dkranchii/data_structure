class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        #this is binary tree where number are lesser than right
        #in order transver
        prev = None
        res = float("inf")
        #apply dfs algorithm for inorder transver
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)
        dfs(root)
        return res
