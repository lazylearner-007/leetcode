class Solution:
	def delNodes(self, root: TreeNode, to_delete):
		self.to_delete = self.listToDict(to_delete)
		self.result = []

		if not self.to_delete.get(root.val):
			self.result.append(root)

		self.traverseNodes(root,parent=None)
        
		return self.result

	def traverseNodes(self,root,parent):
		if not root:
			return

		self.traverseNodes(root.left,root)
		self.traverseNodes(root.right,root)

		if self.to_delete.get(root.val):
			if root.left and root.left.val:
				self.result.append(root.left)
			if root.right and root.right.val:
				self.result.append(root.right)
			if parent:
				if parent.left and parent.left.val == root.val:
					parent.left = None
				elif parent.right and parent.right.val == root.val:
					parent.right = None
		
	def listToDict(self,to_delete):
		Dict = {}
		for i in to_delete:
			Dict[i]=i
		return Dict



		
