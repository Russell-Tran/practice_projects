"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


"""
The key is to mirror everything,
and also keep a special map that maps original
pointers to their mirrored versions.
That way you can fill them out later.
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
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
        