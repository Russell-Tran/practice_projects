def quicksort(arr):
	# https://www.youtube.com/watch?v=SLauY6PpjW4
	# pick random pivot, close in from both sides and swap i j whenever needs to be organized s.t. lessers of pivot swap to left
	# and greators of pivot swap to right
	return None


class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        lower = 0
        upper = len(nums)
        while lower < upper:
            #print(nums[lower:upper])
            i = (upper + lower) // 2
            num = nums[i]
            if num == target:
                return i
            elif num > target:
                upper = i
            else: # num < target
                lower = i + 1
        return -1

def dfs(root):
	# use a stack whereas bfs uses a queue
	return None