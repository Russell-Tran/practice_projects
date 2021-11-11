def binary_search(self, nums, target):
	if len(nums) == 0:
		return -1
	if len(nums) == 1:
		return 0 if nums[0] == target else -1

	lower = 0
	upper = len(nums)
	while lower < upper:
		i = (upper + lower) // 2
		num = nums[i]
		if num == target:
			return i
		elif num > target:
			upper = i
		else:
			lower = i + 1
	return -1


def mergseSort(arr):
	if len(arr) <= 1:
		return

	middle = len(arr) // 2

def reverse(self, head):
	prev = None
	curr = head
	while curr:
		nxt = curr.next
		curr.next = reverse
		prev = curr
		curr = nxt

class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors else []

def clonegraph(node): 
	if not node:
		return None
	seen = set()
	mappings = {}
	stack = [node]
	while len(stack) > 0:
		curr = stack[-1]
		stack.pop(-1)
		seen.add(curr)
		if curr not in mappings:
			mappings[curr] = Node(curr.val)
		mirrored_curr = mappings[curr]
		for neighbor in curr.neighbors:
			if neighbor not in mappings:
				mappings[neighbor] = Node(neighbor.val)
				mirrored_neighbor = mappings[neighbor]
				if mirrored_neighbor not in mirrored_curr.neighbors:
					mirrored_curr.neighbors.append(mirrored_neighbor)
				if neighbor not in seen:
					stack.append(neighbor)
	return mappings[node]

class Solution:
	def generateParenthesis(self, n):
		self.output = []
		self.recurse("", n, n)
		return self.output

	def recurse(self, curr, num_open, num_close):
		if num_close == 0:
			self.output.append(curr)
			return

		if num_close > num_open:
			self.recurse(curr + ")", num_open, num_close-1)

		if num_open > 0:
			self.recurse(curr + "(", num_open-1, num_close)



