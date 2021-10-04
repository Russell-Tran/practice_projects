import heapq
import math

def distance(x, y):
    return math.sqrt(x**2 + y**2)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pqueue = []
        matcher = {}
        for point in points:
            d = distance(*point)
            heapq.heappush(pqueue, (d, point))
        return [heapq.heappop(pqueue)[1] for i in range(k)]