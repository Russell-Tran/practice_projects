class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda interval: interval[0])
        output = [intervals[0]]
        for interval in intervals[1:]:
            tail_start, tail_end = output[-1]
            new_start, new_end = interval
            if new_start <= tail_end:
                output[-1] = [min(tail_start, new_start), max(tail_end, new_end)]
            else:
                output.append(interval)
        return output