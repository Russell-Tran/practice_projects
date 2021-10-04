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
