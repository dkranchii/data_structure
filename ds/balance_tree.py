class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            #visit left node
            left = dfs(root.left)
            #visit right node
            right = dfs(root.right)
            #verify if left and right node has true along
            #sum of length of left + right <= 1
            balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balance , 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
