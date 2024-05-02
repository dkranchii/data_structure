class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #create dfs 
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val) and \
                    dfs(left.left , right.right) and \
                    dfs(left.right , right.left)
        if not root:
            return True
        return dfs(root.left, root.right)
