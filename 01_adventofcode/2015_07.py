def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

class Solution:
	def access(self, token):
		if is_int(token):
			return int(token)
		return self.variables[token]

	def process(self, line):
		line = line.split()
		if line[1] == "->":
			lhs, rhs = line[0], line[2]
			self.variables[rhs] = self.access(lhs)
		elif line[0] == "NOT":
			lhs, rhs = line[1], line[3]
			self.variables[rhs] = ~self.access(lhs)
		elif line[1] == "AND":
			lhs_a, lhs_b, rhs = line[0], line[2], line[4]
			self.variables[rhs] = self.access(lhs_a) & self.access(lhs_b)
		elif line[1] == "OR":
			lhs_a, lhs_b, rhs = line[0], line[2], line[4]
			self.variables[rhs] = self.access(lhs_a) | self.access(lhs_b)
		elif line[1] == "LSHIFT":
			lhs_a, lhs_b, rhs = line[0], line[2], line[4]
			self.variables[rhs] = self.access(lhs_a) << self.access(lhs_b)
		elif line[1] == "RSHIFT":
			lhs_a, lhs_b, rhs = line[0], line[2], line[4]
			self.variables[rhs] = self.access(lhs_a) >> self.access(lhs_b)
		else:
			raise Exception("Unknown!")

	def solve(self):
		self.variables = {}
		with open("2015_07.txt", 'r') as file:
			queue = []
			for line in file:
				try:
					self.process(line)
				except KeyError:
					queue.append(line)
			while len(queue) > 0:
				line = queue[0]
				queue.pop(0)
				try:
					self.process(line)
				except KeyError:
					queue.append(line)
				
		print(self.variables["a"])

				
if __name__ == "__main__":
	Solution().solve()
				