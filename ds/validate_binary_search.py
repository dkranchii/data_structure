class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #create a dfs fuc
        def validate(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (validate(node.left, left, node.val) and 
            validate(node.right, node.val, right))
        
        return validate(root, float("-inf"), float("inf"))
