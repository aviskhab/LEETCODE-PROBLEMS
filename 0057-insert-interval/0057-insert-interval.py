
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        start, end = newInterval

        # 1. Add intervals before newInterval
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        res.append([start, end])

        # 3. Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
