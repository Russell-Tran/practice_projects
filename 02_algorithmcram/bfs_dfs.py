class Node:
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right

def bfs(root):
	if root is None:
		return False
	queue = [root]
	depths = [1]
	curr_depth = 0
	while len(queue) > 0:
		curr = queue[0]
		curr_depth = depths[0]
		queue.pop(0)
		depths.pop(0)

		# if found or something
		# then return True here

		curr_depth += 1
		if curr.left is not None:
			queue.append(curr.left)
			depths.append(curr_depth)
		if curr.right is not None:
			queue.append(curr.right)
			depths.append(curr_depth)

	return False

def dfs(root):
	if root is None:
		return False
	stack = [root]
	depths = [1]
	curr_depth = 0
	while len(stack) > 0:
		curr = queue[-1]
		curr_depth = depths[-1]
		curr.pop(-1)
		depths.pop(-1)

		# if found or something
		# then return True here

		curr_depth += 1
		if curr.right is not None:
			stack.append(curr.right)
			depths.append(curr_depth)
		if curr.left is not None:
			stack.append(curr.left)
			depths.append(curr_depth)

	return False



		