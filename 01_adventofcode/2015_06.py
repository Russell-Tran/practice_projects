class Instruction:
	def __init__(self, line):
		return
	def execute(self, grid):
		return
	def executePartTwo(self, grid):
		return

class TurnInstruction(Instruction):
	def __init__(self, line):
		_, setting, lower_coords, _, upper_coords = line
		self.on = (setting == "on")
		self.lower_row, self.lower_col = [int(c) for c in lower_coords.split(',')]
		self.upper_row, self.upper_col = [int(c) for c in upper_coords.split(',')]

	def execute(self, grid):
		for i in range(self.lower_row, self.upper_row+1):
			for j in range(self.lower_col, self.upper_col+1):
				grid[i][j] = self.on
		return grid

	def executePartTwo(self, grid):
		delta = 1 if self.on else -1
		for i in range(self.lower_row, self.upper_row+1):
			for j in range(self.lower_col, self.upper_col+1):
				grid[i][j] = max(0, grid[i][j] + delta)
		return grid

class ToggleInstruction(Instruction):
	def __init__(self, line):
		_, lower_coords, _, upper_coords = line
		self.lower_row, self.lower_col = [int(c) for c in lower_coords.split(',')]
		self.upper_row, self.upper_col = [int(c) for c in upper_coords.split(',')]

	def execute(self, grid):
		for i in range(self.lower_row, self.upper_row+1):
			for j in range(self.lower_col, self.upper_col+1):
				grid[i][j] = not grid[i][j]
		return grid

	def executePartTwo(self, grid):
		for i in range(self.lower_row, self.upper_row+1):
			for j in range(self.lower_col, self.upper_col+1):
				grid[i][j] += 2
		return grid

def partone():
	grid = [[False] * 1000 for i in range(1000)]

	with open("2015_06.txt", 'r') as file:
		for line in file:
			line = line.split()
			if line[0] == "turn":
				instr = TurnInstruction(line)
			elif line[0] == "toggle":
				instr = ToggleInstruction(line)
			else:
				raise Exception("line[0] = {}".format(line[0]))
			grid = instr.execute(grid)

	answer = sum([1 if cell else 0 for row in grid for cell in row])
	return answer

def parttwo():
	grid = [[0] * 1000 for i in range(1000)]

	with open("2015_06.txt", 'r') as file:
		for line in file:
			line = line.split()
			if line[0] == "turn":
				instr = TurnInstruction(line)
			elif line[0] == "toggle":
				instr = ToggleInstruction(line)
			else:
				raise Exception("line[0] = {}".format(line[0]))
			grid = instr.executePartTwo(grid)

	answer = sum([cell for row in grid for cell in row])
	return answer

if __name__ == "__main__":
	print("Part 1: {}".format(partone()))
	print("Part 2: {}".format(parttwo()))
