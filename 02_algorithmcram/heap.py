"""
heapq is a minheap
the way to create a maxheap is to multiply each key by -1

And of course, if you're trying to return the keys
you have to clean by * -1 on retrieval.
Otherwise, no cleaning necessary for other metadata retrieval
"""


# we do a maxheap here
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        Q = []
        for num, count in counts.items():
            # we want a maxheap so have to multiply by -1
            # What's nice is that you can store a tuple
            # and the priority queue sorts by first element
            # and you can store a bunch of metadata as the other elements
            heapq.heappush(Q, (count * -1, num))
            
        # we access element 1 because we want the metadata ("num id") rather than the count
        return [heapq.heappop(Q)[1]  for i in range(k)]


"""
You can also apparently solve this by 
 - creating a counts dictionary
 - then putting the ids in buckets (n buckets since that's the most any type could have)
 - then flatten the buckets into a single list and return the last k elements
"""
