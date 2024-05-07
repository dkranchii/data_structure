class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Create hashmap
        inorderIdx = {v: i for i, v in enumerate(inorder)}
        def helper(l, r):
            if l > r:
                return None
            # Last element of postorder is root
            root = TreeNode(postorder.pop())
            # Get the index of root from inorder array
            idx = inorderIdx[root.val]
            # Adjust indexing for left and right subtrees
            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)  # Corrected indexing here
            return root

        return helper(0, len(inorder) - 1)
