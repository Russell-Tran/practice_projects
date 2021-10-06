"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def recurse(self, curr, num_open, num_close):
        if num_close == 0:
            self.output.append(curr)
            return
        
        if num_close > num_open:
            self.recurse(curr + ")", num_open, num_close - 1)
            
        if num_open > 0:
            self.recurse(curr + "(", num_open - 1, num_close)
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []
        self.recurse("", n, n)
        return self.output