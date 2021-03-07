class Solution(object):
	def __init__(self):
		self.visited = {}

	def correctBinaryTree(self, root):
		if not root:
			return
		if root.right and self.visited.get(root.right.val):
			return None
		self.visited[root.val] = True
		root.right = self.correctBinaryTree(root.right)
		root.left = self.correctBinaryTree(root.left)

		return root
