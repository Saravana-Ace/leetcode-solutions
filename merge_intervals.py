class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)

        for i in range(len(intervals)):
            if i+1 < len(intervals) and intervals[i+1][1] >= intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            elif i+1 < len(intervals) and intervals[i][0] < intervals[i+1][0] and intervals[i][1] > intervals[i+1][1]:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            else:
                res.append(intervals[i])

        return res