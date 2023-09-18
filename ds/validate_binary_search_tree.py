class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low= - math.inf, high = math.inf):
            # in case of empty tree
            if node is None:
                return True
            # each node value should be between low and high value
            if node.val <= low or node.val >= high:
                return False
            # Varify left and right subtree too
            return (validate(node.right, node.val, high) and validate(node.left, low, node.val))
    
        return validate(root)

  #Time complexity : O(N)\mathcal{O}(N)O(N) since we visit each node exactly once.
  #Space complexity : O(N)\mathcal{O}(N)O(N) since we keep up to the entire tree.
