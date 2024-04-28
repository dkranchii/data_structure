class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #helper function to inorder dfs
        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val
            #check for leef node
            if not node.left and not node.right:
                 return curSum == targetSum
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
        
        return dfs(root, 0)
