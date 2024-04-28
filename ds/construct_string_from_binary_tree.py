class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(root):
            if not root:
                return 
            #add the open parenthesis
            res.append("(")
            #covert to string before adding to res
            res.append(str(root.val))
            if not root.left and root.right:
                res.append("()")
            preorder(root.left)
            preorder(root.right)
            res.append(")")
        preorder(root)
        return "".join(res)[1:-1]
