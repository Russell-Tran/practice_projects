def quicksort(arr):
	# https://www.youtube.com/watch?v=SLauY6PpjW4
	# pick random pivot, close in from both sides and swap i j whenever needs to be organized s.t. lessers of pivot swap to left
	# and greators of pivot swap to right
	return None


class Solution:
    def binary_search(self, nums, target):
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

def mergeSort(arr):
	# https://www.geeksforgeeks.org/merge-sort/
	if len(arr) <= 1:
		return
	middle = len(arr) // 2
	left_arr = arr[:middle] # copy
	right_arr = arr[middle:] # copy
	mergeSort(left_arr)
	mergeSort(right_arr)
	i = 0
	j = 0
	k = 0
	# merge by comparison (put the lesser ones in first)
	while i < len(left_arr) and j < len(right_arr):
		if left_arr[i] < right_arr[j]:
			arr[k] = left_arr[i]
			i += 1
		else:
			arr[k] = right_arr[j]
			j += 1
		k += 1

	# comparison is done; put all the rest in
	while i < len(left_arr):
		arr[k] = left_arr[i]
		i += 1
		k += 1
	while j < len(right_arr):
		arr[k] = right_arr[j]
		j += 1
		k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
