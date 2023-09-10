class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #search for value based on iteration
        while root is not None and root.val !=val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root
