class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
        	root = TreeNode(val)
        if root.val > val:
        	root.left = self.insertIntoBST(root.left,val)

        if root.val < val:
        	root.right = self.insertIntoBST(root.right,val) 

        return root
